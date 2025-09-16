from bs4 import BeautifulSoup
from datetime import datetime

import scraper_definitions as sd

genres_dict = {
    "action"    : "a", "adventure"    : "b", "arcade"     : "c", "casual"     : "d", "fighting"    : "e",
    "highscore" : "f", "horror"       : "g", "cards"      : "h", "platformer" : "i", "puzzle"      : "j",
    "rhythm"    : "k", "role-playing" : "l", "rogue-like" : "m", "shooter"    : "n", "speedrunner" : "o",
    "sports"    : "p", "stealth"      : "q", "strategy"   : "r", "survival"   : "s"}

def scrape_genres(filename, link):
    # open file
    print(f"=== Writing file: {filename}")
    f = open(filename, "w", encoding='utf-8')
    print("cart_id_versionless,genres_tooltip,genres_compact", file=f)

    total_posts = 0
    page_num = 1
    while True:
        print(f"--- Scraping page {page_num}...")
        url = link + str(page_num)
        page = sd.get_with_retries(url, headers=True)
        soup = BeautifulSoup(page.content, "html.parser")

        divs = soup.find_all("div", class_=["card", "bg-dark", "m-2"])
        if divs:
            
            for div in divs:
                genres_compact = ""
                genres_tooltip = div.find_all('div')[-1]["data-original-title"].strip()
                for genre in genres_tooltip.split():
                    genres_compact += genres_dict[genre]
                
                thumb = div.find("img")["src"].split("/")[-1]
                if thumb[0:6] == "pico8_":
                    prefix_size = 6
                else:
                    prefix_size = 4
                
                line  = thumb[prefix_size:].split(".")[0].split("-")[0] + "," # cart ID, versionless
                line += genres_tooltip + ","
                line += genres_compact
                
                print(line, file=f)
                
            print(f"    {len(divs)} carts found in page {page_num}.")
            total_posts += len(divs)
            
        else:
            print("    No carts found.")
            break
        
        page_num += 1 # ready for next loop

    # close file
    print("--- Scraping finished.")        
    print(f"    {total_posts} posts carts in all pages.")
    f.close()
    print("=== Closed file: " + filename)

if __name__ == "__main__":
    start = datetime.now()
    
    scrape_genres(sd.SCRAPED_GAME_GENRES_FILENAME, sd.GAME_GENRES_URL)

    end = datetime.now()
    print(f"    Script ran in {sd.format_timedelta(end - start)}.")