# Star SPLORE's Scraper

## Purpose

This scraper will search [Lexaloffe's BBS](https://www.lexaloffle.com/bbs/) for PICO-8 "Featured Carts".

No other categories or subcategires ("New Carts" in "Releases", "Work in Progess", "Jam" etc.) will be scraped.

## Steps

This scraper consists of 5 steps.

1. Reset the scraper, erasing temp and result files. Carts previously downloaded are not deleted.
2. Scrape "Featured Carts" pages looking for posts linked.
3. Scrape the posts found in the previous step looking for carts.
4. Write result files.
5. Download scraped carts (optional).

Each step is executed by a python script.

## Subdirectories

Starting from the directory where this `README.md` is, files are located on the following subdirectries:

- `scripts`: that's where the python scripts are located.
- `temp`: temporary files will be created here.
- `results`: result files will be created here.
- `carts`: carts will optionally be downloaded here, in .p8.png format.

Aside from `scripts`, all other subdirectories will be created if necessary in step 1.

## Results

Step 4 will create the following files in the `results` subdirectory:

- `featured_carts.html`: this file contains all collected information and links for every scraped cart.
- `featured_carts.lua`: this file will be included by `star_splore.p8`.
- `featured_carts_by_year.lua`: this file will be included by `star_splore_by_year.p8`.
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
python 2_scrape_featured_pages.py
```

- Estimated time to complete: 10 seconds.

### Step 3: scrape featured carts

Type the following command:

```
python 3_scrape_featured_carts.py
```

- Estimated time to complete: 5 minutes.

### Step 4: write result_files

Type the following command:

```
python 4_write_result_files.py
```

- Estimated time to complete: less than 1 second.

### Step 5: download featured carts (optional)

This can be very useful if you want to use STAR SPLORE offline (in a handheld, for example).

Type the following command:

```
python 5_download_featured_carts.py
```

- Estimated time to complete: 3 minutes.

## Retries

If this scraper gets a connection error it employs the simplest possible retry strategy: it simply tries again, no delay involved.
- If the error persists, the script will abort after retrying the same URL 3 times. If that happens, simply wait a while and then run that step again. 
- If you need to run steps 3 or 5 again (the longest ones), the scripts will skip all carts already scraped / downloaded successfully.

## Use responsibly

This scraper sends hundreds of requests to Lexaloffle in rapid succession. Be reasonable, run it as sparingly as possible to avoid overwhelming the server.
