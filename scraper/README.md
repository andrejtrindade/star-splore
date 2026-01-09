# Star SPLORE's Scraper

## Purpose

This scraper will search [Lexaloffe's BBS](https://www.lexaloffle.com/bbs/) for PICO-8 "Featured Carts". 

No other categories or subcategires ("New Carts" in "Releases", "Work in Progess", "Jam" etc.) will be scraped.

The scraper will also search game genres for carts in [Nerdy Teachers' Curated PICO-8 Games](https://nerdyteachers.com/PICO-8/Games/).

## Steps

This scraper consists of 6 steps.

1. Reset the scraper, erasing temp and result files. Carts previously downloaded are not deleted.
2. Scrape "Featured Carts" pages looking for posts linked.
3. Scrape the posts found in the previous step looking for carts.
4. Scrape game genres.
5. Write result files.
6. Download scraped carts (optional).

Each step is executed by a python script.

## Subdirectories

Starting from the directory where this `README.md` is, files are located on the following subdirectries:

- `scripts`: that's where the python scripts are located.
- `adjustments`: files used by the scripts to override some info.
- `temp`: temporary files will be created here.
- `results`: result files will be created here.
- `carts`: carts will optionally be downloaded here, in .p8.png format.

Aside from `scripts` and `adjustments`, the other 3 subdirectories will be created if necessary in step 1.

## Results

Step 5 will create the following files in the `results` subdirectory:

- `featured_carts.html`: this file contains all collected information and links for every scraped cart.
- `featured_carts.lua`: this file will be included by `star_splore.p8`.
- `featured_carts_extra.lua`: metadata that will be written to `star_splore.p8` ROM (GFX/MAP) by  `write_extra_carts.p8`.
- `featured_carts_urls.txt`: this file contains download URLs for all scraped carts. This can be used to download them all with [Wget](https://www.gnu.org/software/wget/).

## Pyhton

To run the scripts you will need python, install it from [python.org](https://www.python.org/).
- The latest version should be fine. If you have any problems, install version 3.13.6.
- Make sure you select the option to add python to your path.
- If you use python for other stuff and know what you are doing, you may create a virtual environment for this scraper. If not, don't bother.

Now, let's install the required dependencies. This scraper needs `requests`, `pandas` and `beautifulsoup4`. I frozen the exact versions so you can install them all with a single command.

Open a command prompt and go to the `scripts` subdirectory. Type the following command:

```
python -m pip install -r requirements.txt
```

Do not close the command prompt, you will need it to run the scripts in the next section.

## Scripts

### Step 1: reset the scraper

Type the following command:

```
python 1_reset_scraper.py
```

- Estimated time to complete: less than 1 second.

### Step 2: scrape "Featured Carts" pages

Type the following command:

```
python 2_scrape_featured_pages.py 1
```

- Estimated time to complete: 10 seconds.

*Note: The argument (the "1" at the end of the command) is the initial page to scrape.*

### Step 3: scrape featured carts

Type the following command:

```
python 3_scrape_featured_carts.py
```

- Estimated time to complete: 5 minutes.

### Step 4: scrape game genres

Type the following command:

```
python 4_scrape_game_genres.py
```

- Estimated time to complete: 40 seconds.

### Step 5: write result_files

Type the following command:

```
python 5_write_result_files.py
```

- Estimated time to complete: less than 1 second.

### Step 6: download featured carts (optional)

This can be very useful if you want to use STAR SPLORE offline (in a handheld, for example).

Type the following command:

```
python 6_download_featured_carts.py
```

- Estimated time to complete: 3 minutes.

## Retries

If this scraper gets a connection error it employs the simplest possible retry strategy: it simply tries again, no delay involved.
- If the error persists, the script will abort after retrying the same URL 3 times. If that happens, simply wait a while and then run that step again. 
- If you need to run steps 3 or 6 again (the longest ones), the scripts will skip all carts already scraped / downloaded successfully.

### Retrying step 2

If step 2 exceeds the BBS search limit, the script will show a warning like this:

```
WARNING: Wait at least 10 minutes, then run this step again with argument 7 to resume scraping featured pages.
```

In my experience, though, this only happens if you modify step 2 to include search terms.

## Use responsibly

This scraper sends hundreds of requests to Lexaloffle in rapid succession. Be reasonable, run it as sparingly as possible to avoid overwhelming the server.
