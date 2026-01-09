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
SCRAPED_GAME_GENRES_FILENAME       = "../temp/4_scraped_game_genres.csv"

# Result files
RESULT_HTML_FILENAME               = "../results/featured_carts.html"
RESULT_LUA_FILENAME                = "../results/featured_carts.lua"
RESULT_LUA_EXTRA_FILENAME          = "../results/featured_carts_extra.lua"
RESULT_URLS_FILENAME               = "../results/featured_carts_urls.txt"

# Carts in RESULT_LUA_FILENAME
MAX_LUA_CARTS                      = 500

# Adjustment files
TITLE_ADJUSTMENTS_FILENAME         = "../adjustments/title_adjustments.csv"
GAME_GENRE_ADJUSTMENTS_FILENAME    = "../adjustments/game_genre_adjustments.csv"

# Lexaloffle links
LEXALOFFLE_BASE_LINK               = "https://www.lexaloffle.com"
LEXALOFFLE_BBS_LINK                = "https://www.lexaloffle.com/bbs/"
LEXALOFFLE_LISTER_LINK             = LEXALOFFLE_BBS_LINK + "lister.php"

# Pages query string
PAGES_QS_FORUM                     = "?cat=7"
PAGES_QS_CARTS_TAB                 = "&carts_tab=1"
PAGES_QS_RELEASES                  = "&sub=2" # "&#sub=2" in BBS link, ajax sends it to lister.php
PAGES_QS_MODE_CARTS                = "&mode=carts"
PAGES_QS_FEATURED_ORDER            = "&orderby=featured"
PAGES_QS_PAGE_NUM                  = "&page=" # originally before mode
PAGES_QS                           = PAGES_QS_FORUM + PAGES_QS_CARTS_TAB + PAGES_QS_RELEASES + PAGES_QS_MODE_CARTS + PAGES_QS_FEATURED_ORDER + PAGES_QS_PAGE_NUM

# Pages URL
FEATURED_PAGES_URL                 = LEXALOFFLE_LISTER_LINK + PAGES_QS

# Nerdy Teachers link
NERDY_TEACHERS_CURATED_LINK        = "https://nerdyteachers.com/PICO-8/Games/"

# Game genres query string
GAME_GENRES_QS_PAGE_NUM            = "?p="

# Game genres URL
GAME_GENRES_URL                    = NERDY_TEACHERS_CURATED_LINK + GAME_GENRES_QS_PAGE_NUM

# Nerdy Teachers website terminates connections when requests do not have headers
NT_HEADERS = {"User-agent": "Mozilla/5.0 (X11; Linux x86_64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"}

def format_timedelta(td):
    minutes, seconds = divmod(td.total_seconds(), 60)
    hours, minutes = divmod(minutes, 60)
    return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"
    
def get_with_retries(url, headers=False):
    retries = 0
    success = False
    while not success:
        try:
            if headers is False:
                response = requests.get(url)
            else:
                response = requests.get(url, headers=NT_HEADERS)
            success = True
        except:
            retries += 1
            print("!!! requests.get() failed, retry: " + str(retries))
            if retries > MAX_NUMBER_OF_RETRIES:
                print("+++ requests.get() failed too many times, aborting...")
                raise   
    return response
