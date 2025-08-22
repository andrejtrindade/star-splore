import requests

# Maximum number of retries
MAX_NUMBER_OF_RETRIES              = 3

# Directories
TEMPORARY_PATH                     = "../temp"
RESULTS_PATH                       = "../results"
DOWNLOAD_PATH                      = "../carts"

# Temporary files
SCRAPED_FEATURED_PAGES_FILENAME    = "../temp/2_scraped_featured_pages.csv"
SCRAPED_FEATURED_CARTS_FILENAME    = "../temp/3_scraped_featured_carts.csv"

# Result files
RESULT_HTML_FILENAME               = "../results/featured_carts.html"
RESULT_LUA_FILENAME                = "../results/featured_carts.lua"
RESULT_URLS_FILENAME               = "../results/featured_carts_urls.txt"

# Lexaloffle links
LEXALOFFLE_BASE_LINK               = "https://www.lexaloffle.com"
LEXALOFFLE_BBS_LINK                = "https://www.lexaloffle.com/bbs/"

# Pages query string
PAGES_QS_FORUM                     = "?cat=7"
PAGES_QS_CARTS_TAB                 = "&carts_tab=1"
PAGES_QS_RELEASES                  = "&sub=2" # originally "&#sub=2", but requests.get() discards everything after the hashtag
PAGES_QS_MODE_CARTS                = "&mode=carts"
PAGES_QS_FEATURED_ORDER            = "&orderby=featured"
PAGES_QS_PAGE_NUM                  = "&page=" # originally before mode
PAGES_QS                           = PAGES_QS_FORUM + PAGES_QS_CARTS_TAB + PAGES_QS_RELEASES + PAGES_QS_MODE_CARTS + PAGES_QS_FEATURED_ORDER + PAGES_QS_PAGE_NUM

# Pages link
FEATURED_PAGES_LINK                = LEXALOFFLE_BBS_LINK + PAGES_QS

def format_timedelta(td):
    minutes, seconds = divmod(td.total_seconds(), 60)
    hours, minutes = divmod(minutes, 60)
    return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"
    
def get_with_retries(url):
    retries = 0
    success = False
    while not success:
        try:
            response = requests.get(url)
            success = True
        except:
            retries += 1
            print("!!! requests.get() failed, retry: " + str(retries))
            if retries > MAX_NUMBER_OF_RETRIES:
                print("+++ requests.get() failed too many times, aborting...")
                raise   
    return response
