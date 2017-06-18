from splinter import Browser

with Browser('firefox', profile="/home/li2266/.mozilla/firefox/2ro8hp3c.default") as browser:
	# AMAZON: ASUS ASUS ROG Strix Radeon RX 580 T8G Gaming 
	url = "https://www.amazon.com/gp/offer-listing/B07197V7C7/?ie=UTF8&condition=all&tag=nisa-20&m=ATVPDKIKX0DER"
	# TEST AMAZON: 1050ti
	url = "https://www.amazon.com/MSI-GeForce-GTX-1050-GAMING/dp/B01MA62JSZ/ref=sr_1_3?s=pc&ie=UTF8&qid=1497761954&sr=1-3&keywords=1050ti"
	browser.visit(url);
	# check login
	
	key_button = browser.find_by_id("oneClickBuyButton");
	if len(key_button) != 0:
		key_button.first.click()
		print("Got!!")
	else:
		print("nothing")