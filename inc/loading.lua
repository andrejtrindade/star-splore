-- loading.lua

loading = {

show = function()
	loading_drawn, loading_failed = false, false
	poke2(0x5e00, cart)
	screen = loading
end,

update = function()
	if loading_drawn and not loading_failed then
		local cart_id = split(filtered_data[cart], ",", false)[5]
		if cart_id != "" then
			load(cart_id, "back to "..c_star.."splore")
			load("#"..split(cart_id, "-", false)[1], "back to "..c_star.."splore")
		end
		loading_failed = true
	end
	if (loading_failed and btnp(4)) menu.show()
end,

draw = function()
	local cart_id = split(filtered_data[cart], ",", false)[5]

	if loading_failed then
		print_center_outline("loading failed", 52, 8, "\^o2ff")
	else
		print_center_outline("loading cart...", 52, 11, "\^o3ff")
	end
	
	print("id:", 0, 64, 5)
	print(sub(cart_id, 1, 32), 0, 70, 6)
	
	if (#cart_id > 32) print(sub(cart_id, 33), 0, 76, 6)
	
	if loading_failed then
		print_commands(nil, "back")
	else
		loading_drawn = true
	end
end

}