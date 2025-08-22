-- main.lua

function _init()
	if not cartdata("ajt_star_splore_1") then
		for i=0,63 do dset(i, 0) end
		poke2(0x5e00, 1)
	end
	
	max_cart = #data
	cart = peek2(0x5e00)
	if (cart > max_cart) cart = max_cart
	
	page, max_page = ceil(cart/10), ceil(max_cart/10)
	
	screen = menu
end

function _update()
	screen.update()
end

function _draw()
	cls()
	screen.draw()
end
