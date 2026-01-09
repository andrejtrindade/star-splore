[#star_splore-3#]

It's like browsing and launching "Featured Carts" in **SPLORE**...

But they are ranked by **STAR**s! And you can filter by **GAME GENRE**!

## Controls

- ⬅️➡️: previous / next page
- ⬆️⬇️: previous / next cart
- 🅾️: filter by *game genre* or by *year*
- ❎: run cart

After you are done with the cart, enter the pause menu and select the last option:
`back to ★SPLORE`

[img]/media/86005/star_splore_demo_2.gif[/img]

## About

**STAR SPLORE** aims to help you discover some of the best PICO-8 carts ever made.

- That's why filters are provided.
- That's why this is a "featured carts only" browser / launcher.
- That's why carts are ranked by stars, the BBS version of "likes".

As imperfect as these metrics may be, they are the ones we have.

*Note: when carts are tied for stars, newer carts rank higher.*

## Interface

[img]/media/86005/star_splore_interface.png[/img]

*Note: when loading carts from the BBS, STAR SPLORE ignores the version number after the ID to get the latest version of the cart.*

## Genres

Game genres for 280 carts were extracted from @NerdyTeachers' excelent [Curated PICO-8 Games](https://nerdyteachers.com/PICO-8/Games/) list. 

I tagged the remaining 229 carts, adding new genres for *collections*, *demos* and *tools*.

If you feel I mistagged a cart, drop a comment!

*Note: STAR SPLORE was actually inspired by NerdyTeachers' [200 Best PICO-8 Games](https://nerdyteachers.com/PICO-8/Games/Top200/) list.*

## Updates

New carts won't show up until **STAR SPLORE** is updated.

**STAR SPLORE** itself is a regular PICO-8 cart after all. It can't fetch newer carts from the BBS automatically.

The date you see on the top right of the screen is **STAR SPLORE**'s current version. This is the date when information was extrated from the BBS and from NerdyTeachers' curated list.

## Offline

**STAR SPLORE** can also run carts offline, as long as they are in the same folder. Just make sure you don't rename cart files after downloading them from the BBS.

Note that running multicarts offline can be tricky, no matter how you launch them. Please refer to [this excelente article](https://nerdyteachers.com/PICO-8/Hardware/70#multicart) from @NerdyTeachers for more information on the subject. Expand section 3, "For Multicart Games".

## Scraper

On [STAR SPLORE's GitHub repository](https://github.com/andrejtrindade/star-splore) you will find the [scraper](https://github.com/andrejtrindade/star-splore/tree/main/scraper) used to extract information from the BBS and from NerdyTeachers' curated list.

### HTML

You can browse all scraped information in [this HTML page](https://github.com/andrejtrindade/star-splore/blob/main/scraper/results/featured_carts.html) (download it and open in your browser).

### Download

The scraper also creates a [file with URLs for all featured carts](https://github.com/andrejtrindade/star-splore/blob/main/scraper/results/featured_carts_urls.txt). You can use that file to download all those carts at once using [Wget](https://www.gnu.org/software/wget/). Please note that downloading carts from the BBS is perfectly legit according to Lexaloffle's [terms of use](https://www.lexaloffle.com/info.php?page=tos).

Dumping these 509 carts together with **STAR SPLORE** in an handheld is a great way to browse and discover some great PICO-8 games on the go, even when you are offline.

## 0.2.7

I didn't know it when I developed and released STAR SPLORE, but you can rank carts by stars on the BBS since at least [May 29, 2025](https://www.lexaloffle.com/bbs/?pid=167739#p). Thanks to @Verb for pointing that out to me.

To do that, go to New Carts or Featured Carts, click the search icon and...

- type `t:week` / `t:month` / `t:year` / `t:halfyear` to search top-starred carts released in the last week / month / year / six months;
- type `tr:202210-202305` to specify an inclusive time range (`tr:2015-2026` is equivalent to using STAR SPLORE);
- type `tr:2022` to search carts from a specific year.

[PICO-8 0.2.7](https://www.lexaloffle.com/bbs/?tid=150992) added this to regular SPLORE, so now you can search for carts ranked by stars over there too.

When you are on your handheld, though, with no wi-fi or no keyboard... Or when you want to browse carts by game genre... **STAR SPLORE** is here to save the day!

## Changelog

[hidden]

- **Version 2026-01-09**: tagged remaining carts, also added extra carts metadata to ROM.
- **Version 2025-09-16**: added filters (by game genre and by year), also adjusted cart names to better fit the interface.
- **Version 2025-08-28**: celebrating 500 featured carts!
- **Version 2025-08-16**: initial version.

[/hidden]