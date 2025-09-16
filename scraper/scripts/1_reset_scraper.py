from pathlib import Path
from datetime import datetime

import scraper_definitions as sd

def make_sure_folder_exists(folder_path):
    print("    Making sure directory exists: " + folder_path)
    p = Path(folder_path)
    p.mkdir(parents=True, exist_ok=True)

def delete_file(filename):
    print("    Deleting if file exists:" + filename)
    f = Path(filename)
    f.unlink(missing_ok=True)
    
if __name__ == "__main__":
    start = datetime.now()
    
    print("=== Creating directories if necessary...")
    make_sure_folder_exists(sd.TEMPORARY_PATH)
    make_sure_folder_exists(sd.RESULTS_PATH)
    make_sure_folder_exists(sd.DOWNLOAD_PATH)
    
    print("=== Deleting temporary files...")
    delete_file(sd.SCRAPED_FEATURED_PAGES_FILENAME)
    delete_file(sd.SCRAPED_FEATURED_CARTS_FILENAME)
    delete_file(sd.SCRAPED_GAME_GENRES_FILENAME)

    print("=== Deleting result files...")
    delete_file(sd.RESULT_HTML_FILENAME)
    delete_file(sd.RESULT_LUA_FILENAME)
    delete_file(sd.RESULT_URLS_FILENAME)

    print("--- Will not delete previously downloaded carts.")
    print("=== Ready to scrape.")
    end = datetime.now()
    print(f"    Script ran in {sd.format_timedelta(end - start)}.")
 