import sys
import re
from bs4 import BeautifulSoup
from datetime import datetime

import scraper_definitions as sd

def scrape_pages(filename, link, first_page):
    # open file
    if first_page == 1:
        print(f"=== Writing file: {filename}")
        f = open(filename, "w", encoding='utf-8')
        print("post_id,thread_link", file=f)
    else:
        print(f"=== Appending to file: {filename}")
        f = open(filename, "a", encoding='utf-8')

    search_limit_exceeded = False
    total_posts = 0
    page_num = first_page
    while True:
        print(f"--- Scraping page {page_num}...")
        url = link + str(page_num)
        page = sd.get_with_retries(url)
        soup = BeautifulSoup(page.content, "html.parser")

        divs_with_id = soup.find_all("div", attrs={"id": re.compile(r'^pdat')})
        if divs_with_id:
            
            for div_with_id in divs_with_id:
                line  = div_with_id["id"][5:] + ","   # post_id
                line += div_with_id.find("a")["href"] # thread_link
                print(line, file=f)
                
            print(f"    {len(divs_with_id)} posts found in page {page_num}.")
            total_posts += len(divs_with_id)
            
        else:
            if re.search(r"Search rate limit exceeded", page.text) is not None:
                print("!!! WARNING: Search rate limit exceeded! Please come back later.")
                search_limit_exceeded = True
            else:
                print("    No posts found.")
            break
        
        page_num += 1 # ready for next loop

    # close file
    print("--- Scraping finished.")        
    print(f"    {total_posts} posts found in all pages.")
    f.close()
    print("=== Closed file: " + filename)
    
    if search_limit_exceeded:
        print(f"!!! WARNING: Wait at least 10 minutes, then run this step again with argument {page_num} to resume scraping featured pages.")

if __name__ == "__main__":
    start = datetime.now()
    
    if len(sys.argv) > 1:
        try:
            first_page = int(sys.argv[1])
        except:
            sys.exit("!!! ERROR: First argument (initial page) is not integer.")
    else:
        sys.exit("!!! ERROR: First argument (initial page) was not provided.")
    
    scrape_pages(sd.SCRAPED_FEATURED_PAGES_FILENAME, sd.FEATURED_PAGES_URL, first_page)

    end = datetime.now()
    print(f"    Script ran in {sd.format_timedelta(end - start)}.")
