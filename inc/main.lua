-- main.lua

function _init()
	if not cartdata(cartdata_id) then
		for i=0,63 do dset(i, 0) end
	end
	
	load_cartdata(true)
	
	-- default data for empty cartdata / original cartdata with no filters
	if (cart   == 0) cart   = 1
	if (filter == 0) filter = 1
	if (genre  == 0) genre  = 1
	if (year   == 0) year   = 2025
	
	filtering.show(false)
end

function _update()
	screen.update()
end

function _draw()
	cls()
	screen.draw()
end

function load_cartdata(load_cart)
	
	if(load_cart) cart = peek2(0x5e00)
	
	filter = peek2(0x5e02)
	genre  = peek2(0x5e04)
	year   = peek2(0x5e06)
end
