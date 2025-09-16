-- filters.lua

filter_names = {"all featured carts","filter by game genre","filter by year"}

filters = {

update = function()
	if (btnp(2) and filter > 1) filter -= 1
	if (btnp(3) and filter < 3) filter += 1

	if btnp(4) then
		load_cartdata(false)
		menu.show()
	end

	if btnp(5) then
		if (filter == 1) filtering.show(true)
		if (filter == 2) screen = filter_genre
		if (filter == 3) screen = filter_year
	end
end,

draw = function()
	print_center_outline("filters", 1, 7, "\^o5ff")
	local y = 48
	for i=1,3 do
		rectfill(0, y, 127, y+6, (filter == i and 13 or 1))
		print_center(filter_names[i], y+1, (filter == i and 7 or 6))
		y += 8
	end
	print_commands("select", "back")
end
	
}
