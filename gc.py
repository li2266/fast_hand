from splinter import Browser

with Browser('firefox', profile="/home/li2266/.mozilla/firefox/2ro8hp3c.default") as browser:

	# url_dict = {"AMAZON: ASUS ASUS ROG Strix Radeon RX 580 T8G Gaming ": "https://www.amazon.com/gp/offer-listing/B07197V7C7/?ie=UTF8&condition=all&tag=nisa-20&m=ATVPDKIKX0DER"}
	url_dict = {"MSI GeForce GTX 1050 Ti DirectX 12 GTX 1050 Ti GAMING X 4G 4GB": "https://www.newegg.com/Product/Product.aspx?Item=N82E16814137054&cm_re=1050ti-_-14-137-054-_-Product"}
	limitation = 10

	amount = 0

	# TEST AMAZON: 1050ti
	# url = "https://www.amazon.com/MSI-GeForce-GTX-1050-GAMING/dp/B01MA62JSZ/ref=sr_1_3?s=pc&ie=UTF8&qid=1497761954&sr=1-3&keywords=1050ti"
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
				key_button = browser.find_by_id("oneClickBuyButton");
				if len(key_button) != 0:
					key_button.first.click()
					print("Got {0} in Amazon".format(key))
					amount += 1
				else:
					print("{0} is out of stock".format(key))

			# this is in newegg
			elif value.find("newegg") != -1:
				print("looking at {0} in Newegg".format(key))
				if browser.is_text_present("ADD TO CART", wait_time=2):
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

				else:
					print("out of stock")

		break