-- menu.lua

menu = {

show = function()
	max_cart = #filtered_data
	if (cart > max_cart) cart = max_cart
	page, max_page = ceil(cart/10), ceil(max_cart/10)
	
	screen = menu
end,

update = function()
	if btnp(0) and page > 1 then
		cart -= 10
		page -= 1
	end
	if btnp(1) and page < max_page then
		cart += 10
		page += 1
	end
	
	if (btnp(2) and cart%10 != 1) cart -= 1
	if (btnp(3) and cart%10 != 0) cart += 1
	
	if (cart > max_cart) cart = max_cart
	
	if (btnp(4)) screen = filters
	if (btnp(5)) loading.show()
end,

draw = function()
	local from = cart - (cart-1)%10
	local to = min(from + 9, max_cart)

	print("\^o5ff"..c_star.."splore", 1, 1, 0)
	print_right(version, 1, 5)
	filter_string = "all"
	if (filter == 2) filter_string = genre_names[genre]
	if (filter == 3) filter_string = tostr(year)
	print("\^o5ff"..filter_string, 61-2*#filter_string, 1, 7)

	y = 8
	for i=from,to do
		local cart_data = split(filtered_data[i], ",", false)
	
		if i == cart then
			rectfill(0, y, 127, y+32, 13)
			y += 1
			
			local genres_str = ""
			local compact = cart_data[6]
			for j=1,#compact do
				genres_str ..= genre_names[ord(compact[j])-96]
				if (j < #compact) genres_str ..= " "
			end
			if (#genres_str == 0) genres_str = "untagged"
			
			-- rank
			print("#", 1, y, 5)
			print(i, 5, y, 1)

			print_center(cart_data[2], y, 1) -- date
			print_stars(tostr(cart_data[1]), y, 1, 10) -- stars
			print_center(ellipsis(cart_data[3], 31), y+7, 7) -- title
			print_center(ellipsis("by "..cart_data[4], 31), y+13, 6) -- author
			print_center(ellipsis(genres_str, 31), y+20, 1) -- genres
			print_right(ellipsis("id: "..cart_data[5], 31), y+26, 5) -- id
		
			y += 33
		else
			rectfill(0, y, 127, y+6, 1)
			y += 1
			
			-- rank
			print("#", 1, y, 5)
			print(i, 5, y, 13)

			print_stars(tostr(cart_data[1]), y, 13, 4) -- stars
			print_center(ellipsis(cart_data[3], 20), y, 6) -- title
			
			y+= 7
		end
	end
	
	y = 114
	rrectfill(0, y, 128, 7, 1, 5)
	y += 1
	
	color(0)
	if (page > 1)  print(c_left, 1, y)
	if (page < max_page) print(c_right, 120, y)
	s = "page "..page.." of ".. max_page
	print_center(s, y)

	print_commands("play", "filters")
end

}
