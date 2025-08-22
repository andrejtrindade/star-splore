# Star SPLORE's Scraper

## Purpose

This scraper will search [Lexaloffe's BBS](https://www.lexaloffle.com/bbs/) for PICO-8 "Featured Carts".

No other categories or subcategires ("New Carts" in "Releases", "Work in Progess", "Jam" etc.) will be scraped.

## Steps

This scraper consists of 5 steps.

1. Reset the scraper, erasing results produced by previous scrapes. Carts previously downloaded are not deleted.
2. Scrape pages in the "Featured Carts" subcategory for linked posts.
3. Scrape the first cart in each post found in the previous step.
4. Write result files.
5. Download scraped carts (optional).

Each step is executed by a python script.

## Subdirectories

Starting from directory where this `README.md` file is, scraper files are located on the following subdirectries:

- `scripts`: that's where the python scripts are located.
- `temp`: temporary files will be created here.
- `results`: result files will be created here (more on that below).
- `carts`: carts will optionally be downloaded here, in .p8.png format.

Aside from `scripts`, all other subdirectories will be created if necessary in step 1.

## Results

Step 4 will create the following files in the `results` subdirectory:

- `featured_carts.html`: this file contains all collected information and links for every scraped cart.
- `featured_carts.lua`: this file will be included by `star_splore.p8`.
- `featured_carts_urls.txt`: this file contains download URLs for all scraped carts.

## Pyhton

To run the scripts you will need python, install it from [python.org](https://www.python.org/).
- The latest version should be fine. If you have any problems, install version 3.13.6.
- Make sure you select the option to add python to your path.
- If you use python for other stuff and know what you are doing, you may create a virtual environment for this scraper. If not, don't bother.

Now, let's install the required dependencies.

Open a command prompt and go to the `scripts` subdirectory. Do not close this command prompt, you will need it to run the scripts later.

### Option 1: install dependencies using requirements.txt

This is the safest option, as it will install the exact version of each package frozen during the scraper development. Type the following command:

```
python -m pip install -r requirements.txt
```

### Option 2: install the latest version of each dependency

You can try installing the latest version of each package used by the scripts, but be aware that this can potentially create problems if future versions introduce any breaking changes.

Anyway, these commands should be typed one by one.

```
python -m pip install requests
python -m pip install beautifulsoup4
python -m pip install pandas
```

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

### Step 3: scrape the first cart in each post linked in the "Featured Carts" pages

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

If this scraper gets a connection error it employs the simplest possible retry strategy: it simply tries again.
- If the error persists, the script will abort after retrying the same URL 3 times. If that happens, simply wait a while and then run that step again. 
- If you need to run steps 3 or 5 again (the longer ones), the scripts will skip all carts already scraped / downloaded successfully.

## Use responsibly

This scraper sends hundreds of requests to Lexaloffle in rapid succession. Be reasonable, run it as sparingly as possible to avoid overwhelming the server.
