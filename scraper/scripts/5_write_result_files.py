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
<tr><th>Rank</th><th>Stars</th><th>Published</th><th>Thread</th><th>Post</th><th>Cart</th><th>Author</th><th>Game Genres</th></tr>
"""

HTML_END = """
</table>
</body>
</html>
"""

def find_genres(df_genres, cart_id_versionless, compact):
    genres = ""
    genres_rows = df_genres[df_genres["cart_id_versionless"] == cart_id_versionless]
    if not genres_rows.empty:
        if compact:
            genres += genres_rows.iloc[0]["genres_compact"]
        else:
            genres += genres_rows.iloc[0]["genres_tooltip"]
    return genres

def write_html(df_genres, df_sorted, html_filename):
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
            html_content += f"<td>{find_genres(df_genres, cart_id_versionless, False)}</td></tr>\n"
            
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
    
def write_lua(df_genres, df_sorted, df_titles, lua_filename):
    print(f"    Formatting Lua...")
    
    lua_content = f"version = \"{date.today()}\"\n\n"
    lua_content += "data = {\n"

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

            lua_content += "\""
            lua_content += f"{stars},"
            lua_content += f"{cart_year},"
            lua_content += f"{title},"
            lua_content += f"{cart.author_name[0:29].lower()},"
            lua_content += f"{cart_id},"
            lua_content += f"{find_genres(df_genres, cart_id_versionless, True)}"
            lua_content += "\",\n"
        except:
            print("!!! Error at cart: ")
            print(cart)
            raise

    print(f"    Total carts added to Lua: {carts}")

    lua_content += "}"

    # write lua file
    file_object = open(lua_filename, "w", encoding='utf-8')
    file_object.write(lua_content)
    file_object.close()
    print("=== Lua file written: " + lua_filename)

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
    
    print("--- Reading file: " + sd.SCRAPED_FEATURED_CARTS_FILENAME)
    df_carts = pd.read_csv(sd.SCRAPED_FEATURED_CARTS_FILENAME, encoding='utf-8', keep_default_na=False)
    
    print("--- Reading file: " + sd.TITLE_ADJUSTMENTS_FILENAME)
    df_titles = pd.read_csv(sd.TITLE_ADJUSTMENTS_FILENAME, encoding='utf-8', keep_default_na=False)   

    print("--- Sorting carts...")
    df_sorted = df_carts.sort_values(by=["stars", "date_time"], ascending=[False, False])

    write_html(df_genres, df_sorted, sd.RESULT_HTML_FILENAME)
    write_lua(df_genres, df_sorted, df_titles, sd.RESULT_LUA_FILENAME)
    extract_urls(df_sorted, sd.RESULT_URLS_FILENAME)

    end = datetime.now()
    print(f"    Script ran in {sd.format_timedelta(end - start)}.")
