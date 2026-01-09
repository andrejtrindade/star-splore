-- filtering.lua

filtering = {

show = function(cart_reset)
	if (cart_reset)  cart = 1
	if (filter != 2) genre = 1
	if (filter != 3) year  = 2025
	if filter == 1 then
		filtered_data = data
		save_cartdata()
		menu.show()
	else
		filtering_drawn = false
		screen = filtering
	end
end,

update = function()
	if filtering_drawn then
		filtered_data = {}
		for i=1,#data do
			local cart_data = data[i]
			if filter == 2 then
				local compact = split(cart_data)[6]
				for j=1,#compact do
					if (ord(compact[j]) == genre + 96) add(filtered_data, cart_data)
				end
			end
			if filter == 3 then
				local y = split(cart_data)[2]
				if (y == year) add(filtered_data, cart_data)
			end
		end
		
		save_cartdata()
		menu.show()
	end
end,

draw = function()
	print_center_outline("filtering...", 62, 11, "\^o3ff")
	filtering_drawn = true
end

}

function save_cartdata()
	poke2(0x5e00, cart)
	poke2(0x5e02, filter)
	poke2(0x5e04, genre)
	poke2(0x5e06, year)
	poke2(0x5e08, cartdata_version)
end
