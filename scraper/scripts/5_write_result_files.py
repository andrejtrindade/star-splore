import pandas as pd
from datetime import datetime, date

import scraper_definitions as sd

HTML_BEGIN = """
<!DOCTYPE html>
<html>
<head><title>STAR SPLORE's scraper results</title></head>
<style>
table, th, td {
  border: 1px solid black;
}
</style><body>
<h1>STAR SPLORE's scraper results</h1>
<table>
<tr><th>Rank</th><th>Stars</th><th>Published</th><th>Thread</th><th>Post</th><th>Cart</th><th>Author</th><th>Game Genres</th><th>Tagged by</th></tr>
"""

HTML_END = """
</table>
</body>
</html>
"""

genres_dict = {
    "action"       : "a",
	"adventure"    : "b",
	"arcade"       : "c",
	"cards"        : "d",
	"casual"       : "e",
	"collection"   : "f",
	"demo"         : "g",
	"fighting"     : "h",
    "highscore"    : "i",
	"horror"       : "j",
	"platformer"   : "k",
	"puzzle"       : "l",
    "rhythm"       : "m",
	"role-playing" : "n",
	"rogue-like"   : "o",
	"shooter"      : "p",
	"speedrunner"  : "q",
    "sports"       : "r",
	"stealth"      : "s",
	"strategy"     : "t",
	"survival"     : "u",
	"tool"         : "v"}

def find_genres(df_genres, df_genre_adjustments, thread_link, cart_id_versionless, compact):
    genres = ""
    tagged_by = ""
    
    genres_rows = df_genres[df_genres["cart_id_versionless"] == cart_id_versionless]
    if not genres_rows.empty:
        genres += genres_rows.iloc[0]["genres_tooltip"]
        if genres != "":
            tagged_by = "Nerdy Teachers"
    
    genre_adjustments_rows = df_genre_adjustments[df_genre_adjustments["thread_link"] == thread_link]
    if not genre_adjustments_rows.empty:
        if tagged_by == "Nerdy Teachers":
            print("!!! WARNING: overwriting NerdyTeacher - " + cart_id_versionless)
        genres = genre_adjustments_rows.iloc[0]["genres_tooltip"]
        tagged_by = "STAR SPLORE"

    if compact:
        genres_compact = ""
        
        for genre in genres.split():
            genres_compact += genres_dict[genre]
            
        return genres_compact
    
    else:
        return genres, tagged_by

def write_html(df_genres, df_genre_adjustments, df_sorted, html_filename):
    print(f"    Formatting HTML...")
    html_content = HTML_BEGIN

    carts = 0
    for cart in df_sorted.itertuples():
        carts += 1
        
        try:
            stars = int(cart.stars)
        except ValueError:
            stars = 0
            
        try:
            html_content += f"<tr><td>{carts}</td>"
            html_content += f"<td>{stars}</td>"
            html_content += f"<td>{cart.date_time}</td>"
            html_content += f"<td><a href=\"{sd.LEXALOFFLE_BBS_LINK}{cart.thread_link}\">{cart.thread_title}</a></td>"
            html_content += f"<td><a href=\"{cart.post_link}\">post</a></td>"
            
            if cart.cart_title == "":
                html_content += "<td></td>"
            else:
                html_content += f"<td><a href=\"{cart.cart_link}\">{cart.cart_title}</a></td>"
            
            if cart.author_name == "":
                html_content += "<td></td>"
            else:
                html_content += f"<td><a href=\"{cart.author_link}\">{cart.author_name}</a></td>"
                
            cart_id_versionless = cart.cart_link.split("/")[-1].split(".")[0].split("-")[0]
            genres, tagged_by = find_genres(df_genres, df_genre_adjustments, cart.thread_link, cart_id_versionless, False)
            html_content += f"<td>{genres}</td><td>{tagged_by}</td></tr>\n"
            
        except:
            print("!!! Error at cart: ")
            print(cart)
            raise

    print(f"    Total carts added to HTML: {carts}")

    html_content += HTML_END

    # write html
    f = open(html_filename, "w", encoding='utf-8')
    f.write(html_content)
    f.close()
    print("=== HTML file written: " + html_filename)
    
def write_lua(df_genres, df_genre_adjustments, df_sorted, df_titles, lua_filename, max_lua_carts, lua_extra_filename):
    print(f"    Formatting Lua...")
    
    lua_content = f"version = \"{date.today()}\"\n\n"
    lua_content += "data = {\n"
    
    lua_content_extra = "data = {\n"

    carts = 0
    for cart in df_sorted.itertuples():
        carts += 1
        
        try:
            stars = int(cart.stars)
        except ValueError:
            stars = 0

        try:
            cart_id             = cart.cart_link.split("/")[-1].split(".")[0]
            cart_id_versionless = cart_id.split("-")[0]
            cart_year           = cart.date[0:4]
            
            title_rows = df_titles[df_titles["thread_link"] == cart.thread_link]
            if not title_rows.empty:
                title = title_rows.iloc[0]["thread_title"][0:32].lower()
            else:
                title = cart.thread_title[0:32].lower()

            content  = "\""
            content += f"{stars},"
            content += f"{cart_year},"
            content += f"{title},"
            content += f"{cart.author_name[0:29].lower()},"
            content += f"{cart_id},"
            content += f"{find_genres(df_genres, df_genre_adjustments, cart.thread_link, cart_id_versionless, True)}"
            content += "\",\n"
        except:
            print("!!! Error at cart: ")
            print(cart)
            raise

        if carts > max_lua_carts:
            lua_content_extra += content
        else:
            lua_content += content
        

    print(f"    Total carts added to Lua: {carts}")

    lua_content += "} -- extra data is in cart rom"
    
    lua_content_extra += "}"

    # write lua file
    file_object = open(lua_filename, "w", encoding='utf-8')
    file_object.write(lua_content)
    file_object.close()
    print("=== Lua file written: " + lua_filename)

    # write lua extra file
    file_object = open(lua_extra_filename, "w", encoding='utf-8')
    file_object.write(lua_content_extra)
    file_object.close()
    print("=== Lua file written: " + lua_extra_filename)

def extract_urls(df_sorted, urls_filename):
    print(f"    Extracting URLs...")
    
    urls_content = ""
    carts = 0
    for cart in df_sorted.itertuples():
        carts += 1
        urls_content += cart.cart_link + "\n"

    print(f"    Total URLs extracted: {carts}")
 
    # write URLs file
    file_object = open(urls_filename, "w", encoding='utf-8')
    file_object.write(urls_content)
    file_object.close()
    print("=== URLs file written: " + urls_filename) 

if __name__ == "__main__":
    start = datetime.now()

    print("--- Reading file: " + sd.SCRAPED_GAME_GENRES_FILENAME)
    df_genres = pd.read_csv(sd.SCRAPED_GAME_GENRES_FILENAME, encoding='utf-8', keep_default_na=False)
    
    print("--- Reading file: " + sd.GAME_GENRE_ADJUSTMENTS_FILENAME)
    df_genre_adjustments = pd.read_csv(sd.GAME_GENRE_ADJUSTMENTS_FILENAME, encoding='utf-8', keep_default_na=False)
    
    print("--- Reading file: " + sd.SCRAPED_FEATURED_CARTS_FILENAME)
    df_carts = pd.read_csv(sd.SCRAPED_FEATURED_CARTS_FILENAME, encoding='utf-8', keep_default_na=False)
    
    print("--- Reading file: " + sd.TITLE_ADJUSTMENTS_FILENAME)
    df_titles = pd.read_csv(sd.TITLE_ADJUSTMENTS_FILENAME, encoding='utf-8', keep_default_na=False)   

    print("--- Sorting carts...")
    df_sorted = df_carts.sort_values(by=["stars", "date_time"], ascending=[False, False])

    write_html(df_genres, df_genre_adjustments, df_sorted, sd.RESULT_HTML_FILENAME)
    write_lua(df_genres, df_genre_adjustments, df_sorted, df_titles, sd.RESULT_LUA_FILENAME, sd.MAX_LUA_CARTS, sd.RESULT_LUA_EXTRA_FILENAME)
    extract_urls(df_sorted, sd.RESULT_URLS_FILENAME)

    end = datetime.now()
    print(f"    Script ran in {sd.format_timedelta(end - start)}.")
