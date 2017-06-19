from splinter import Browser

with Browser('firefox', profile="/home/li2266/.mozilla/firefox/2ro8hp3c.default") as browser:

	# url_dict = {"AMAZON: ASUS ASUS ROG Strix Radeon RX 580 T8G Gaming ": "https://www.amazon.com/gp/offer-listing/B07197V7C7/?ie=UTF8&condition=all&tag=nisa-20&m=ATVPDKIKX0DER"}
	url_dict = {"ASUS Radeon RX 580 O4G Dual-fan OC Edition GDDR5: AMAZON": "https://www.amazon.com/dp/B071CMPRZZ/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "ASUS Radeon RX 580 DirectX 12 DUAL-RX580-O8G 8GB 256-Bit GDDR5 newegg": "https://www.newegg.com/Product/Product.aspx?Item=N82E16814126196", "ASUS Radeon RX 580 8GB Dual-fan OC Edition GDDR5": "https://www.amazon.com/dp/B071L1VGQW/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "ASUS Radeon RX 580 DirectX 12 DUAL-RX580-O8G 8GB 256-Bit GDDR5":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814126199", "ASUS ROG-STRIX-RX580-O8G-GAMINGOC Edition GDDR5":"https://www.amazon.com/dp/B071D8YQJD/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "ASUS Radeon RX 580 DirectX 12 DUAL-RX580-O8G 8GB 256-Bit GDDR5":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814126193", "ASUS ASUS ROG Strix Radeon RX 580 T8G Gaming":"https://www.amazon.com/dp/B07197V7C7/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "ASUS Radeon RX 580 DirectX 12 DUAL-RX580-O8G 8GB 256-Bit GDDR5":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814126192", "Gigabyte AORUS Radeon RX 580 4GB":"https://www.amazon.com/dp/B06Y3V1K81/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "Gigabyte AORUS Radeon RX 580 8GB":"https://www.amazon.com/dp/B06Y46X4L9/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "GIGABYTE AORUS Radeon RX 580 DirectX 12 GV-RX580AORUS-8GD 8GB":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814125961", "Gigabyte Radeon RX 580 Gaming 4GB":"https://www.amazon.com/dp/B06Y44TWF3/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "Gigabyte Radeon RX 580 Gaming 8GB Graphic Cards GV-RX580GAMING-8GD":"https://www.amazon.com/dp/B06Y3ZQPY6/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "GIGABYTE Radeon RX 580 DirectX 12 GV-RX580GAMING-8GD 8GB 256-Bit GDDR5 ":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814125962", "Gigabyte AORUS Radeon RX 580 XTR 8GB":"https://www.amazon.com/dp/B06Y45GQ1L/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "GIGABYTE AORUS Radeon RX 580 DirectX 12 GV-RX580XTRAORUS-8GD 8GB":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814125960", "MSI RX 580 8G Graphic Cards":"https://www.amazon.com/dp/B071RW7SCT/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "MSI Radeon RX 580 DirectX 12 RX 580 8G 8GB 256-Bit GDDR5":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814137135", "MSI VGA Graphic Cards RX 580 ARMOR 4G OC":"https://www.amazon.com/dp/B06XZZ93FQ/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "MSI VGA Graphic Cards RX 580 ARMOR 8G OC":"https://www.amazon.com/dp/B06XZQMMHJ/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "MSI Radeon RX 580 DirectX 12 RX 580 ARMOR 8G OC 8GB 256-Bit GDDR5":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814137118", "MSI VGA Graphic Cards RX 580 GAMING X 4G":"https://www.amazon.com/dp/B06XZRWT8D/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "MSI Radeon RX 580 DirectX 12 RX 580 GAMING X 4G 4GB 256-Bit GDDR5":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814137119", "MSI VGA Graphic Cards RX 580 GAMING X 8G":"https://www.amazon.com/dp/B06Y19NMP3/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "MSI Radeon RX 580 DirectX 12 RX 580 GAMING X 8G 8GB 256-Bit GDDR5":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814137117", "MSI R580GXP8 PCI-Express Video Graphic Cards":"https://www.amazon.com/dp/B071VDCCJM/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "MSI Radeon RX 580 DirectX 12 RX 580 GAMING X+ 8G 8GB 256-Bit GDDR5 ":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814137116", "PowerColor RED DRAGON Radeon RX 580 DirectX 12 AXRX 580 4GBD5-3DHD/OC 4GB":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814131715", "PowerColor AXRX 580 4GBD5-3DHDV2/OC AMD Radeon RX 580 4GB Red Dragon V2 Graphics Card":"https://www.amazon.com/dp/B0714B1GNZ/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "PowerColor RED DRAGON Radeon RX 580 DirectX 12 AXRX 580 4GBD5-3DHDV2/OC 4GB":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814131719", "PowerColor RED DEVIL Radeon RX 580 DirectX 12 AXRX 580 8GBD5-3DH/OC 8GB":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814131713", "PowerColor RED DRAGON Radeon RX 580 DirectX 12 AXRX 580 8GBD5-3DHD/OC 8GB":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814131714", "PowerColor AXRX 580 8GBD5-3DHDV2/OC AMD Radeon RX 580 8GB Red Dragon V2 Graphics Card":"https://www.amazon.com/dp/B0711QH8ZS/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "PowerColor RED DRAGON Radeon RX 580 DirectX 12 AXRX 580 8GBD5-3DHDV2/OC 8GB":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814131720", "PowerColor VGA Graphic Cards AXRX580 8GBD5-3DHG/OC":"https://www.amazon.com/dp/B06ZZCV9SY/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "PowerColor RED DEVIL Golden Radeon RX 580 DirectX 12 AXRX 580 8GBD5-3DHG/OC 8GB ":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814131712", "Sapphire Radeon NITRO+ RX 580 4GB GDDR5 PCI-E Dual HDMI / DVI-D / Dual DP w/ Backplate (UEFI)":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814202279", "Sapphire Radeon NITRO+ RX 580 8GB GDDR5 PCI-E Dual HDMI / DVI-D / Dual DP w/ backplate (UEFI)":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814202280", "Sapphire Radeon NITRO+ RX 580 8GB GDDR5 PCI-E Dual HDMI / DVI-D / Dual DP w/ backplate Limited Edition (UEFI)":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814202281", "Sapphire Radeon PULSE RX 580 4GB GDDR5 PCI-E Dual HDMI / DVI-D / Dual DP OC w/ Backplate (UEFI)":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814202277", "Sapphire Radeon PULSE RX 580 8GB GDDR5 PCI-E Dual HDMI / DVI-D / Dual DP OC w/ Backplate (UEFI)":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814202278", "Sapphire 11265-01-20G Radeon NITRO+ RX 580 8GB GDDR5":"https://www.amazon.com/dp/B071QX74F9/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "Sapphire 11265-09-20G Radeon PULSE RX 580 4GB GDDR5":"https://www.amazon.com/dp/B071CPJZSX/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "VisionTek Radeon RX 580 DirectX 12 900960 8GB ":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814129327", "XFX GTR-S Black Edition RX 580 8GB OC+ 1450Mhz DDR5 ":"https://www.amazon.com/dp/B071XZ867C/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "XFX GTR-S Black Edition Radeon RX 580 DirectX 12 RX-580A8DBW6 8GB ":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814150796", "XFX GTS XXX Edition RX 580 4GB OC+ 1386MHz DDR5":"https://www.amazon.com/dp/B07115GPN7/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "XFX Radeon RX 580 DirectX 12 RX-580P427D6 4GB 256-Bit DDR5":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814150797", "XFX GTS XXX Edition RX 580 4GB OC+ 1386Mhz DDR5":"https://www.amazon.com/dp/B06ZXRLX3H/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "XFX GTS Black Core Edition RX 580 8GB OC+ 1405MHz DDR5 3xDP HDMI DVI RX-580P828D6":"https://www.amazon.com/dp/B072B6W44N/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "XFX GTS Black Core Edition Radeon RX 580 DirectX 12 RX-580P828D6 8GB OC":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814150794", "XFX GTS Black Edition RX 580 8GB OC+ 1425Mhz DDR5":"https://www.amazon.com/dp/B071CD6K6Z/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "XFX GTS XXX Edition RX 580 8GB OC+ 1386Mhz DDR5":"https://www.amazon.com/dp/B06Y66K3XD/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "XFX Radeon RX 580 DirectX 12 RX-580P8DFD6 8GB ":"https://www.newegg.com/Product/Product.aspx?Item=2VV-000U-00003&cm_re=XFX_RX-580P8DFD6-_-2VV-000U-00003-_-Product", "XFX Gtr-S black Edition Rx 580 8GB":"https://www.amazon.com/dp/B06ZYB4C18/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "ASUS ROG Strix Radeon RX 570 O4G Gaming OC Edition GDDR5":"https://www.amazon.com/dp/B06Y5WGXX3/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "Gigabyte AORUS Radeon RX 570 4GB Graphic Cards GV-RX570AORUS-4GD":"https://www.amazon.com/dp/B06Y43ZKFF/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "GIGABYTE AORUS Radeon RX 570 DirectX 12 GV-RX570AORUS-4GD 4GB ":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814125965", "MSI VGA Graphic Cards RX 570 ARMOR 4G OC":"https://www.amazon.com/dp/B06Y144RLK/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "MSI Radeon RX 570 DirectX 12 RX 570 ARMOR 4G OC 4GB 256-Bit GDDR5":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814137123", "MSI VGA Graphic Cards RX 570 GAMING X 4G":"https://www.amazon.com/dp/B06Y15M48C/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "PowerColor AXRX 570 4GBD5-3DH/OC Video Card":"https://www.amazon.com/dp/B071DF8SJV/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "PowerColor RED DEVIL Radeon RX 570 DirectX 12 AXRX 570 4GBD5-3DH/OC 4GB ":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814131716", "PowerColor VGA - AXRX 570 4GBD5-3DHD/OC":"https://www.amazon.com/dp/B06ZYRRW9T/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "PowerColor RED DRAGON Radeon RX 570 DirectX 12 AXRX 570 4GBD5-3DHD/OC 4GB":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814131717", "Sapphire Radeon NITRO+ RX 570 4GB GDDR5 PCI-E Dual HDMI / DVI-D / Dual DP w/ Backplate (UEFI)":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814202285", "Sapphire Radeon NITRO+ RX 570 8GB GDDR5 PCI-E Dual HDMI / DVI-D / Dual DP w/ Backplate (UEFI)":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814202282", "Sapphire Radeon PULSE RX 570 ITXI 4GB GDDR5 PCI-E HDMI / DVI-D / DP (UEFI)":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814202284", "Sapphire Radeon PULSE RX 570 4GB GDDR5 PCI-E Dual HDMI / DVI-D / Dual DP OC w/ Backplate (UEFI)":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814202283", "Sapphire 11266-04-20G Radeon PULSE RX 570 4GB GDDR5":"https://www.amazon.com/dp/B06ZY21842/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "Sapphire 11266-06-20G Radeon PULSE RX 570 ITX 4GB GDDR5":"https://www.amazon.com/dp/B06ZYWX744/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "Sapphire 11266-09-20G Radeon NITRO+ RX 570 8GB GDDR5":"https://www.amazon.com/dp/B071XNH5BC/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "Sapphire 11266-14-20G Radeon NITRO+ RX 570 4GB GDDR5":"https://www.amazon.com/dp/B071CF1JFV/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "VisionTek Products 900961 Radeon RX 570 Overclocked 4GB GDDR5":"https://www.amazon.com/dp/B071Y3T737/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "XFX RS XXX Edition RX 570 4GB OC+ 1284MHz DDR5 3xDP HDMI DVI w/Custom Backplate":"https://www.amazon.com/dp/B06ZXY43VC/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "XFX RS XXX Edition Radeon RX 570 DirectX 12 RX-570P427D6 4GB OC+ ":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814150795", "XFX Rs XXX Edition Rx 570 4GB OC+":"https://www.amazon.com/dp/B06Y64PV2X/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER"}

	limitation = 10

	amount = 0

	while True:
		if amount > limitation:
			break
		for key, value in url_dict.items():
			if amount > limitation:
				break
			browser.visit(value);
			# this is amazon
			if value.find("amazon") != -1:
				print("looking at {0} in Amazon".format(key))
				key_button = browser.find_by_id("oneClickBuyButton")
				if len(key_button) != 0:
					print("IN STOCK!!!!!!!!!!!!!!!!!!!!!!!!!")
					while True:
						browser.find_by_id("oneClickBuyButton").first.click()
						print("Got {0} in Amazon".format(key))
						amount += 1
						if amount > 10:
							break
						browser.visit(value);
						key_button = browser.find_by_id("oneClickBuyButton")
						if len(key_button) == 0:
							break
				else:
					print("{0} is out of stock".format(key))

			# this is in newegg
			elif value.find("newegg") != -1:
				print("looking at {0} in Newegg".format(key))
				if browser.is_text_present("ADD TO CART"):
					print("IN STOCK!!!!!!!!!!!!!!!!!!!!!!!!!")
					while True:
						# start processing
						# add to cart
						add_cart = browser.find_by_css("button.btn.btn-primary.btn-wide")
						if len(add_cart) != 0:
							add_cart.first.click()
							print("add to cart successfully")
						else:
							print("fail to add to cart")

						# go to cart
						browser.visit("https://secure.newegg.com/Shopping/ShoppingCart.aspx")

						# got to checkout
						checkout = browser.find_by_css("a.button.button-primary.has-icon-right")
						if len(checkout) != 0:
							#checkout.first.click()
							browser.click_link_by_href("javascript:attachDelegateEvent((function(){Biz.GlobalShopping.ShoppingCart.checkOut('True')}));")
							print("go to checkout successfully")
						else:
							print("fail to checkout")

						# if need login?
						require_login = browser.find_by_id("submit")
						if len(require_login) != 0:
							#require_login.first.click()
							browser.click_link_by_id("submit")
							print("login")

						# finish shipping
						shipping = browser.find_by_css("a.button.button-primary.button-override.has-icon-right")
						if len(shipping) != 0:
							#shipping.first.click()
							browser.click_link_by_href("javascript:Biz.GlobalShopping.CheckOut.continueToBilling();")
							print("shipping successfully")
						else:
							print("fail to shipping")

						# input cvv
						cvv = browser.find_by_id("creditCardCVV2")
						if len(cvv) != 0:
							cvv.fill("469")
							print("input cvv successfully")
						else:
							print("fail to input cvv")

						# finish billing
						billing = browser.find_by_css("a.button.button-primary.button-override.has-icon-right")
						if len(billing) != 0:
							browser.click_link_by_href("javascript:Biz.GlobalShopping.CheckOut.continueToReview(1);")
							#billing.first.click()
							print("finish billing successfully")
						else:
							print("fail to billing")

						# final term checkbox
						term = browser.find_by_name("AgreeOrNot")
						if len(term) != 0:
							browser.check("AgreeOrNot")
							print("agree term")
						else:
							print("fail to agree term")

						# place order
						place_order = browser.find_by_id("SubmitOrder")
						if len(place_order) != 0:
							browser.click_link_by_href("javascript:Biz.GlobalShopping.CheckOut.submitOrder();")
							#place_order.first.click()
							print("place order successfully")
							amount += 1
						else:
							print("fail to place the order")

						if amount > 10:
							break
						browser.visit(value);
						if not browser.is_text_present("ADD TO CART"):
							break

				else:
					print("out of stock")

		break