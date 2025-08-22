import re
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

import scraper_definitions as sd

# .csv columns
CART_CSV_COLUMNS = "post_id,thread_link,thread_title,cart_title,post_link,author_name,author_link,cart_link,date,date_time,stars"

# Posts QS and link
POSTS_QUERY_STRING                 = "?pid="
POSTS_LINK                         = sd.LEXALOFFLE_BBS_LINK + POSTS_QUERY_STRING

def scrape_posts(pages_filename, carts_filename):
    print(f"--- Reading file: {pages_filename}")
    df_pages = pd.read_csv(pages_filename, encoding='utf-8')
    
    print(f"--- Reading file: {carts_filename}")
    try:
        df_carts = pd.read_csv(carts_filename, encoding='utf-8', keep_default_na=False)
    except FileNotFoundError:
        df_carts = pd.DataFrame(columns=CART_CSV_COLUMNS.split(","))

    # overwrite carts file
    print(f"=== Writing file: {carts_filename}")
    f = open(carts_filename, "w", encoding='utf-8')
    print(CART_CSV_COLUMNS, file=f)
    
    count = 0
    skips = 0
    adds  = 0
    for post in df_pages.itertuples():
        carts = df_carts.loc[df_carts["post_id"] == post.post_id]
        if len(carts) >= 1:
            skips += 1
            cart = carts.iloc[0]
            line  = f"{cart.post_id},"
            line += f"{cart.thread_link},"
            line += f"{cart.thread_title},"
            line += f"{cart.cart_title},"
            line += f"{cart.post_link},"
            line += f"{cart.author_name},"
            line += f"{cart.author_link},"
            line += f"{cart.cart_link},"
            line += f"{cart.date},"
            line += f"{cart.date_time},"
            line += f"{cart.stars}"
        else:
            adds += 1
            line  = f"{post.post_id},"
            line += f"{post.thread_link},"
            
            url = POSTS_LINK + str(post.post_id)
            page2 = sd.get_with_retries(url)
            soup2 = BeautifulSoup(page2.content, "html.parser")
            
            thread_title = soup2.find("title").text.strip().replace(",","")
            line += f"{thread_title},"
            
            cart_player = soup2.find("div", attrs={"id": re.compile(r'^cart_player_dormant')})
            if cart_player is not None:
                
                # cart_title, post_link, author_name, author_link
                links = cart_player.find_all("a")
                for link in links:
                    line += link.text.strip().replace(",","") + "," + link["href"] + ","
                
                # cart_link
                cart = soup2.find('a', attrs={"title": "Open Cartridge File"})
                line += sd.LEXALOFFLE_BASE_LINK + cart["href"] + ","
                
                # date, date_time
                date = cart.find_next("span")
                line += date.text.strip().replace(",","") + "," + date["title"].strip().replace(",","") + ","
                
                # stars
                star = date.find_next('div', attrs={"title": "Give this post a star"})
                star_counter = star.find_next_sibling("div")
                if star_counter is not None:
                    line += star_counter.text.strip().replace(",","")
                else:
                    line += str(0)                        
            
            # no cart player
            else:
                print(f"    Found a post with no carts in trhead {thread_title}. Link: {post.thread_link}")
                line += ",,,,,,,"
                    
        print(line, file=f)
        count += 1
        if count % 10 == 0:
            print(f"    {count} posts scraped ({skips} skipped).")
        
    # close file
    print("--- Scraping finished.")
    print(f"    Total posts scraped: {count} ({skips} skipped).")
    f.close()
    print("=== Closed file: " + carts_filename)

if __name__ == "__main__":
    start = datetime.now()
    
    scrape_posts(sd.SCRAPED_FEATURED_PAGES_FILENAME, sd.SCRAPED_FEATURED_CARTS_FILENAME)

    end = datetime.now()
    print(f"    Script ran in {sd.format_timedelta(end - start)}.")
