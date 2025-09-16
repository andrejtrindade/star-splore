-- filter_year.lua

filter_year = {

update = function()
	if (btnp(2) and year <  2025) year += 1
	if (btnp(3) and year >  2015) year -= 1

	if (btnp(4)) screen = filters
	if (btnp(5)) filtering.show(true)
end,

draw = function()
	print_center_outline("filter by year", 1, 7, "\^o5ff")
	local y = 16
	for i=2025,2015,-1 do
		rectfill(1, y, 127, y+6, (year == i and 13 or 1))
		print_center(tostr(i), y+1, (year == i and 7 or 6))
		y += 8
	end
	print_commands("select", "back")
end
	
}