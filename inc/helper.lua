-- helper.lua

-- print functions

function print_center(s, y, c)
	if c then
		print(s, 64-2*#s, y, c)
	else
		print(s, 64-2*#s, y)
	end
end

function print_center_outline(s, y, c, o)
	if c then
		print(o..s, 64-2*#s, y, c)
	else
		print(o..s, 64-2*#s, y)
	end
end

function print_right(s, y, c)
	if c then
		print(s, 128-4*#s, y, c)
	else
		print(s, 128-4*#s, y)
	end
end

function print_stars(stars, y, c1, c2)
	local x = 128 - #stars*4
	print(stars, x, y, c1)
	print(c_star, x-8, y, c2)
end

function print_command(s)
	print_center(s, 122, 6)
	print(c_x, 52-2*#s, 122, 11)
	print(c_o, 68+2*#s, 122, 8)
end

-- string functions

function ellipsis(s, n)
	if (#s < n) return s
	if (n < 4) return sub(s, 1, n)
	return sub(s, 1, n-3).."..."
end
