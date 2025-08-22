-- menu.lua

menu = {

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
	
	if btnp(4) or btnp(5) then
		loading.show()
	end
end,

draw = function()
	local from = cart - (cart-1)%10
	local to = min(from + 9, max_cart)

	print("\^o5ff"..c_star.."splore", 1, 1, 0)
	print_right(latest_cart, 1, 5)

	y = 8
	for i=from,to do
		local cart_data = split(data[i], ",", false)
	
		if i == cart then
			rectfill(0, y, 127, y+32, 13)
			y += 1
			
			-- rank
			print("#", 1, y, 5)
			print(i, 5, y, 1)

			print_center(cart_data[2], y, 1) -- date
			print_stars(tostr(cart_data[1]), y, 1, 10) -- stars
			print_center(ellipsis(cart_data[3], 31), y+10, 7) -- title
			print_center(ellipsis("by "..cart_data[4], 31), y+16, 6) -- author
			print_right(ellipsis("id: "..cart_data[5], 31), y+26, 1) -- id
		
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

	print_command("play")
end

}
