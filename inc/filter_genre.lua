-- filter_genre.lua

genre_names = split("action,adventure,arcade,casual,fighting,highscore,horror,cards,platformer,puzzle,rhythm,role-playing,rogue-like,shooter,speedrunner,sports,stealth,strategy,survival,untagged")

filter_genre = {

update = function()
	if (btnp(0) and genre    >= 11) genre -= 10
	if (btnp(1) and genre    <= 10) genre += 10
	if (btnp(2) and genre%10 !=  1) genre -= 1
	if (btnp(3) and genre%10 !=  0) genre += 1

	if (btnp(4)) screen = filters
	if (btnp(5)) filtering.show(true)
end,

draw = function()
	print_center_outline("filter by game genre", 1, 7, "\^o5ff")
	local y = 20
	for i=1,10 do
		rectfill(1, y, 63, y+6, (genre == i and 13 or 1))
		print_center(genre_names[i], y+1, (genre == i and 7 or 6), true)
		rectfill(65, y, 127, y+6, (genre == i+10 and 13 or 1))
		print_center(genre_names[i+10], y+1, (genre == i+10 and 7 or 6), false, true)
		y += 8
	end
	print_commands("select", "back")
end
	
}