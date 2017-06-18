from splinter import Browser
from pyquery import PyQuery as pq

with Browser('firefox', profile="/home/li2266/.mozilla/firefox/2ro8hp3c.default") as browser:

	url_dict = {"AMAZON: ASUS ASUS ROG Strix Radeon RX 580 T8G Gaming ", "https://www.amazon.com/gp/offer-listing/B07197V7C7/?ie=UTF8&condition=all&tag=nisa-20&m=ATVPDKIKX0DER"}

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