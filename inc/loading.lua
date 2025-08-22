-- loading.lua

loading = {

show = function()
	loading_drawn, loading_failed = false, false
	poke2(0x5e00, cart)
	screen = loading
end,

update = function()
	if loading_drawn and not loading_failed then
		local cart_id = split(data[cart], ",", false)[5]
		if cart_id != "" then
			load(cart_id, "back to "..c_star.."splore")
			load("#"..split(cart_id, "-", false)[1], "back to "..c_star.."splore")
		end
		loading_failed = true
	end
	if (loading_failed and (btnp(4) or btnp(5))) screen = menu
end,

draw = function()
	local cart_data = split(data[cart], ",", false)
	local cart_id = cart_data[5]

	if loading_failed then
		print_center_outline("loading failed", 18, 8, "\^o2ff")
	else
		print_center_outline("loading cart...", 18, 11, "\^o3ff")
	end
	
	print([[title:


author:


published:


id:]], 0, 30, 5)
	print(ellipsis(cart_data[3], 31)..[[



]]..ellipsis(cart_data[4], 28)..[[



]]..cart_data[2]..[[



]]..sub(cart_id, 1, 32), 0, 36, 6)
	
	if (#cart_id > 32) print(sub(cart_id, 33), 0, 96, 6)
	
	if loading_failed then
		print_command("back")
	else
		loading_drawn = true
	end
end

}