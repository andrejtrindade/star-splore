import pathlib
import urllib
from datetime import datetime

import scraper_definitions as sd

def retrieve_with_retries(file_link, file_name):
    retries = 0
    success = False
    while not success:
        try:
            urllib.request.urlretrieve(file_link, file_name)
            success = True
        except:
            retries += 1
            print("!!! urllib.request.urlretrieve() failed, retry: " + str(retries))
            if retries > MAX_NUMBER_OF_RETRIES:
                print("+++ urllib.request.urlretrieve() failed too many times, aborting...")
                raise   

def download_carts(urls_filename, download_path):
    files = 0
    skips = 0
    print(f"--- Reading file: {urls_filename}")
    with open(urls_filename, "r") as f:
        for index, line in enumerate(f):
            files += 1
            file_link = line.strip()
            file_name = download_path + "/" + file_link.split("/")[-1]
            
            if not pathlib.Path(file_name).is_file():
                retrieve_with_retries(file_link, file_name)
            else:
                skips += 1
                
            if files % 10 == 0:
                print(f"    {files - skips} carts downloaded, ({skips} skipped).")

        print(f"=== {files - skips} carts downloaded, {skips} skipped.")

if __name__ == "__main__":
    start = datetime.now()
    
    download_carts(sd.RESULT_URLS_FILENAME, sd.DOWNLOAD_PATH)

    end = datetime.now()
    print(f"    Script ran in {sd.format_timedelta(end - start)}.")
