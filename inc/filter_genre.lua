-- filter_genre.lua

genre_names = split("action,adventure,arcade,cards,casual,collection,demo,fighting,highscore,horror,platformer,puzzle,rhythm,role-playing,rogue-like,shooter,speedrunner,sports,stealth,strategy,survival,tool")

filter_genre = {

update = function()
	if (btnp(0) and genre    >= 12) genre -= 11
	if (btnp(1) and genre    <= 11) genre += 11
	if (btnp(2) and genre%11 !=  1) genre -= 1
	if (btnp(3) and genre%11 !=  0) genre += 1

	if (btnp(4)) screen = filters
	if (btnp(5)) filtering.show(true)
end,

draw = function()
	print_center_outline("filter by game genre", 1, 7, "\^o5ff")
	local y = 20
	for i=1,11 do
		rectfill(1, y, 63, y+6, (genre == i and 13 or 1))
		print_center(genre_names[i], y+1, (genre == i and 7 or 6), true)
		rectfill(65, y, 127, y+6, (genre == i+11 and 13 or 1))
		print_center(genre_names[i+11], y+1, (genre == i+11 and 7 or 6), false, true)
		y += 8
	end
	print_commands("select", "back")
end
	
}