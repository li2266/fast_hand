from splinter import Browser
import time

# with Browser('firefox', profile="/home/li2266/.mozilla/firefox/2ro8hp3c.default") as browser: 
with Browser('firefox', profile="/home/pengli/.mozilla/firefox/m9nast68.default") as browser:
	# url_dict = {"AMAZON: ASUS ASUS ROG Strix Radeon RX 580 T8G Gaming ": "https://www.amazon.com/gp/offer-listing/B07197V7C7/?ie=UTF8&condition=all&tag=nisa-20&m=ATVPDKIKX0DER"}
	url_dict = {"ASUS Radeon RX 580 O4G Dual-fan OC Edition GDDR5: AMAZON": "https://www.amazon.com/dp/B071CMPRZZ/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "ASUS Radeon RX 580 DirectX 12 DUAL-RX580-O8G 8GB 256-Bit GDDR5 newegg": "https://www.newegg.com/Product/Product.aspx?Item=N82E16814126196", "ASUS Radeon RX 580 8GB Dual-fan OC Edition GDDR5": "https://www.amazon.com/dp/B071L1VGQW/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "ASUS Radeon RX 580 DirectX 12 DUAL-RX580-O8G 8GB 256-Bit GDDR5":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814126199", "ASUS ROG-STRIX-RX580-O8G-GAMINGOC Edition GDDR5":"https://www.amazon.com/dp/B071D8YQJD/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "ASUS Radeon RX 580 DirectX 12 DUAL-RX580-O8G 8GB 256-Bit GDDR5":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814126193", "ASUS ASUS ROG Strix Radeon RX 580 T8G Gaming":"https://www.amazon.com/dp/B07197V7C7/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "ASUS Radeon RX 580 DirectX 12 DUAL-RX580-O8G 8GB 256-Bit GDDR5":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814126192", "Gigabyte AORUS Radeon RX 580 4GB":"https://www.amazon.com/dp/B06Y3V1K81/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "Gigabyte AORUS Radeon RX 580 8GB":"https://www.amazon.com/dp/B06Y46X4L9/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "GIGABYTE AORUS Radeon RX 580 DirectX 12 GV-RX580AORUS-8GD 8GB":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814125961", "Gigabyte Radeon RX 580 Gaming 4GB":"https://www.amazon.com/dp/B06Y44TWF3/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "Gigabyte Radeon RX 580 Gaming 8GB Graphic Cards GV-RX580GAMING-8GD":"https://www.amazon.com/dp/B06Y3ZQPY6/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "GIGABYTE Radeon RX 580 DirectX 12 GV-RX580GAMING-8GD 8GB 256-Bit GDDR5 ":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814125962", "Gigabyte AORUS Radeon RX 580 XTR 8GB":"https://www.amazon.com/dp/B06Y45GQ1L/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "GIGABYTE AORUS Radeon RX 580 DirectX 12 GV-RX580XTRAORUS-8GD 8GB":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814125960", "MSI RX 580 8G Graphic Cards":"https://www.amazon.com/dp/B071RW7SCT/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "MSI Radeon RX 580 DirectX 12 RX 580 8G 8GB 256-Bit GDDR5":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814137135", "MSI VGA Graphic Cards RX 580 ARMOR 4G OC":"https://www.amazon.com/dp/B06XZZ93FQ/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "MSI VGA Graphic Cards RX 580 ARMOR 8G OC":"https://www.amazon.com/dp/B06XZQMMHJ/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "MSI Radeon RX 580 DirectX 12 RX 580 ARMOR 8G OC 8GB 256-Bit GDDR5":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814137118", "MSI VGA Graphic Cards RX 580 GAMING X 4G":"https://www.amazon.com/dp/B06XZRWT8D/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "MSI Radeon RX 580 DirectX 12 RX 580 GAMING X 4G 4GB 256-Bit GDDR5":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814137119", "MSI VGA Graphic Cards RX 580 GAMING X 8G":"https://www.amazon.com/dp/B06Y19NMP3/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "MSI Radeon RX 580 DirectX 12 RX 580 GAMING X 8G 8GB 256-Bit GDDR5":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814137117", "MSI R580GXP8 PCI-Express Video Graphic Cards":"https://www.amazon.com/dp/B071VDCCJM/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "MSI Radeon RX 580 DirectX 12 RX 580 GAMING X+ 8G 8GB 256-Bit GDDR5 ":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814137116", "PowerColor RED DRAGON Radeon RX 580 DirectX 12 AXRX 580 4GBD5-3DHD/OC 4GB":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814131715", "PowerColor AXRX 580 4GBD5-3DHDV2/OC AMD Radeon RX 580 4GB Red Dragon V2 Graphics Card":"https://www.amazon.com/dp/B0714B1GNZ/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "PowerColor RED DRAGON Radeon RX 580 DirectX 12 AXRX 580 4GBD5-3DHDV2/OC 4GB":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814131719", "PowerColor RED DEVIL Radeon RX 580 DirectX 12 AXRX 580 8GBD5-3DH/OC 8GB":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814131713", "PowerColor RED DRAGON Radeon RX 580 DirectX 12 AXRX 580 8GBD5-3DHD/OC 8GB":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814131714", "PowerColor AXRX 580 8GBD5-3DHDV2/OC AMD Radeon RX 580 8GB Red Dragon V2 Graphics Card":"https://www.amazon.com/dp/B0711QH8ZS/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "PowerColor RED DRAGON Radeon RX 580 DirectX 12 AXRX 580 8GBD5-3DHDV2/OC 8GB":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814131720", "PowerColor VGA Graphic Cards AXRX580 8GBD5-3DHG/OC":"https://www.amazon.com/dp/B06ZZCV9SY/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "PowerColor RED DEVIL Golden Radeon RX 580 DirectX 12 AXRX 580 8GBD5-3DHG/OC 8GB ":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814131712", "Sapphire Radeon NITRO+ RX 580 4GB GDDR5 PCI-E Dual HDMI / DVI-D / Dual DP w/ Backplate (UEFI)":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814202279", "Sapphire Radeon NITRO+ RX 580 8GB GDDR5 PCI-E Dual HDMI / DVI-D / Dual DP w/ backplate (UEFI)":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814202280", "Sapphire Radeon NITRO+ RX 580 8GB GDDR5 PCI-E Dual HDMI / DVI-D / Dual DP w/ backplate Limited Edition (UEFI)":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814202281", "Sapphire Radeon PULSE RX 580 4GB GDDR5 PCI-E Dual HDMI / DVI-D / Dual DP OC w/ Backplate (UEFI)":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814202277", "Sapphire Radeon PULSE RX 580 8GB GDDR5 PCI-E Dual HDMI / DVI-D / Dual DP OC w/ Backplate (UEFI)":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814202278", "Sapphire 11265-01-20G Radeon NITRO+ RX 580 8GB GDDR5":"https://www.amazon.com/dp/B071QX74F9/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "Sapphire 11265-09-20G Radeon PULSE RX 580 4GB GDDR5":"https://www.amazon.com/dp/B071CPJZSX/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "VisionTek Radeon RX 580 DirectX 12 900960 8GB ":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814129327", "XFX GTR-S Black Edition RX 580 8GB OC+ 1450Mhz DDR5 ":"https://www.amazon.com/dp/B071XZ867C/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "XFX GTR-S Black Edition Radeon RX 580 DirectX 12 RX-580A8DBW6 8GB ":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814150796", "XFX GTS XXX Edition RX 580 4GB OC+ 1386MHz DDR5":"https://www.amazon.com/dp/B07115GPN7/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "XFX Radeon RX 580 DirectX 12 RX-580P427D6 4GB 256-Bit DDR5":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814150797", "XFX GTS XXX Edition RX 580 4GB OC+ 1386Mhz DDR5":"https://www.amazon.com/dp/B06ZXRLX3H/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "XFX GTS Black Core Edition RX 580 8GB OC+ 1405MHz DDR5 3xDP HDMI DVI RX-580P828D6":"https://www.amazon.com/dp/B072B6W44N/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "XFX GTS Black Core Edition Radeon RX 580 DirectX 12 RX-580P828D6 8GB OC":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814150794", "XFX GTS Black Edition RX 580 8GB OC+ 1425Mhz DDR5":"https://www.amazon.com/dp/B071CD6K6Z/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "XFX GTS XXX Edition RX 580 8GB OC+ 1386Mhz DDR5":"https://www.amazon.com/dp/B06Y66K3XD/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "XFX Radeon RX 580 DirectX 12 RX-580P8DFD6 8GB ":"https://www.newegg.com/Product/Product.aspx?Item=2VV-000U-00003&cm_re=XFX_RX-580P8DFD6-_-2VV-000U-00003-_-Product", "XFX Gtr-S black Edition Rx 580 8GB":"https://www.amazon.com/dp/B06ZYB4C18/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", 
	"ASUS ROG Strix Radeon RX 570 O4G Gaming OC Edition GDDR5":"https://www.amazon.com/dp/B06Y5WGXX3/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "Gigabyte AORUS Radeon RX 570 4GB Graphic Cards GV-RX570AORUS-4GD":"https://www.amazon.com/dp/B06Y43ZKFF/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "GIGABYTE AORUS Radeon RX 570 DirectX 12 GV-RX570AORUS-4GD 4GB ":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814125965", "MSI VGA Graphic Cards RX 570 ARMOR 4G OC":"https://www.amazon.com/dp/B06Y144RLK/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "MSI Radeon RX 570 DirectX 12 RX 570 ARMOR 4G OC 4GB 256-Bit GDDR5":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814137123", "MSI VGA Graphic Cards RX 570 GAMING X 4G":"https://www.amazon.com/dp/B06Y15M48C/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "PowerColor AXRX 570 4GBD5-3DH/OC Video Card":"https://www.amazon.com/dp/B071DF8SJV/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "PowerColor RED DEVIL Radeon RX 570 DirectX 12 AXRX 570 4GBD5-3DH/OC 4GB ":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814131716", "PowerColor VGA - AXRX 570 4GBD5-3DHD/OC":"https://www.amazon.com/dp/B06ZYRRW9T/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "PowerColor RED DRAGON Radeon RX 570 DirectX 12 AXRX 570 4GBD5-3DHD/OC 4GB":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814131717", "Sapphire Radeon NITRO+ RX 570 4GB GDDR5 PCI-E Dual HDMI / DVI-D / Dual DP w/ Backplate (UEFI)":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814202285", "Sapphire Radeon NITRO+ RX 570 8GB GDDR5 PCI-E Dual HDMI / DVI-D / Dual DP w/ Backplate (UEFI)":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814202282", "Sapphire Radeon PULSE RX 570 ITXI 4GB GDDR5 PCI-E HDMI / DVI-D / DP (UEFI)":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814202284", "Sapphire Radeon PULSE RX 570 4GB GDDR5 PCI-E Dual HDMI / DVI-D / Dual DP OC w/ Backplate (UEFI)":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814202283", "Sapphire 11266-04-20G Radeon PULSE RX 570 4GB GDDR5":"https://www.amazon.com/dp/B06ZY21842/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "Sapphire 11266-06-20G Radeon PULSE RX 570 ITX 4GB GDDR5":"https://www.amazon.com/dp/B06ZYWX744/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "Sapphire 11266-09-20G Radeon NITRO+ RX 570 8GB GDDR5":"https://www.amazon.com/dp/B071XNH5BC/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "Sapphire 11266-14-20G Radeon NITRO+ RX 570 4GB GDDR5":"https://www.amazon.com/dp/B071CF1JFV/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "VisionTek Products 900961 Radeon RX 570 Overclocked 4GB GDDR5":"https://www.amazon.com/dp/B071Y3T737/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "XFX RS XXX Edition RX 570 4GB OC+ 1284MHz DDR5 3xDP HDMI DVI w/Custom Backplate":"https://www.amazon.com/dp/B06ZXY43VC/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "XFX RS XXX Edition Radeon RX 570 DirectX 12 RX-570P427D6 4GB OC+ ":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814150795", "XFX Rs XXX Edition Rx 570 4GB OC+":"https://www.amazon.com/dp/B06Y64PV2X/ref=olp_product_details?_encoding=UTF8&me=ATVPDKIKX0DER", "XFX Radeon RX 470 DirectX":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814150781", "GIGABYTE Radeon RX 570 DirectX 12 GV-RX570GAMING-4GD 4GB 256-Bit GDDR5":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814125966&ignorebbr=1",
"XFX RADEON RX 470 4GB":"https://www.amazon.com/gp/offer-listing/B01JHQXGEE/ref=dp_olp_0?ie=UTF8&condition=all&tag=nisa-20&m=ATVPDKIKX0DER",
"XFX Radeon RX 470 RS 4GB GDDR5":"https://www.amazon.com/gp/offer-listing/B01JM2DFLC/ref=dp_olp_0?ie=UTF8&condition=all&tag=nisa-20&m=ATVPDKIKX0DER",
"XFX Radeon RX 470 RS Black Edition": "https://www.newegg.com/Product/Product.aspx?Item=N82E16814150777", 
"XFX Radeon RX 470 RS Triple X ": "https://www.newegg.com/Product/Product.aspx?Item=N82E16814150776",
"XFX RX-470P436BM AMD Radeon 4GB ": "https://www.amazon.com/gp/offer-listing/B01JTNU652/ref=dp_olp_0?ie=UTF8&condition=all&tag=nisa-20&m=ATVPDKIKX0DER",
"SAPPHIRE NITRO+ Radeon RX 470 100407NT+8GOCL 8GB 256-Bit ":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814202226",
"SAPPHIRE NITRO+ Radeon RX 470 ":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814202229",
"SAPPHIRE Radeon RX 470 DirectX 12 100407-4GOCL 4GB 256-Bit ":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814202230",
"PowerColor RED DRAGON Radeon RX 470 DirectX":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814131699",
"PowerColor RED DEVIL Radeon RX 470 DirectX 12 AXRX 470 4G":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814131696",
"PowerColor RED DEVIL Radeon RX 470 DirectX 12 ":"https://www.amazon.com/gp/offer-listing/B01K54DJQW/ref=dp_olp_0?ie=UTF8&condition=all&tag=nisa-20&m=ATVPDKIKX0DER",
"PowerColor AMD Radeon RED DEVIL RX 470 4GB ":"https://www.amazon.com/gp/offer-listing/B01JGNP79K/ref=dp_olp_0?ie=UTF8&condition=all&tag=nisa-20&m=ATVPDKIKX0DER",
"MSI Radeon RX 470 DirectX 12 RX 470 ":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814137025",
"MSI GAMING Radeon RX 470 GDDR5 8GB ":"https://www.amazon.com/gp/offer-listing/B01KCWZHTO/ref=dp_olp_0?ie=UTF8&condition=all&tag=nisa-20&m=ATVPDKIKX0DER",
"MSI Radeon RX 470 DirectX 12 RX 470 GAMING X 4G 4GB ":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814137024",
"MSI GAMING Radeon RX 470 GDDR5 4GB":"https://www.amazon.com/gp/offer-listing/B01JS9F9K4/ref=dp_olp_0?ie=UTF8&condition=all&tag=nisa-20&m=ATVPDKIKX0DER",
"GIGABYTE Radeon RX 470 DirectX 12 ": "https://www.newegg.com/Product/Product.aspx?Item=N82E16814125910",
"GIGABYTE Radeon RX 470 DirectX 12 GV-RX470G1 GAMING-4G 4GB ":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814125896",
"Gigabyte Radeon Rx 470 G1 Gaming 4GB":"https://www.amazon.com/gp/offer-listing/B01JNTXM2Q/ref=dp_olp_0?ie=UTF8&condition=all&tag=nisa-20&m=ATVPDKIKX0DER",
"ASUS ROG STRIX Radeon RX 470 4GB":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814126124",
"ASUS ROG STRIX Radeon Rx 470 ":"https://www.amazon.com/gp/offer-listing/B01JS2UFDM/ref=dp_olp_0?ie=UTF8&condition=all&tag=nisa-20&m=ATVPDKIKX0DER",
# "ASUS ROG STRIX Radeon RX 470 4GB DP 1.4 HDMI 2.0 AMD Gaming Graphics Card":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814126123",
"ASUS ROG STRIX Radeon Rx 470 4GB":"https://www.amazon.com/gp/offer-listing/B01JS2UFO6/ref=dp_olp_0?ie=UTF8&condition=all&tag=nisa-20&m=ATVPDKIKX0DER", "XFX RX-480P8LFB6 RADEON 8GB":"https://www.amazon.com/gp/offer-listing/B01JM1C5BY/ref=dp_olp_0?ie=UTF8&condition=all&tag=nisa-20&m=ATVPDKIKX0DER",
"XFX Radeon GTR RX 480 DirectX 12 RX-480":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814150782",
"XFX RX-480P8DFA6 AMD Radeon GTR 8GB GDDR5":"https://www.amazon.com/gp/offer-listing/B01J8CCUL2/ref=dp_olp_0?ie=UTF8&condition=all&tag=nisa-20&m=ATVPDKIKX0DER",
"XFX Radeon GTR RX 480 DirectX 12 RX-480P8DBA6 ":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814150773",
"XFX RX-480P836BM AMD":"https://www.amazon.com/gp/offer-listing/B01KCWZ0DM/ref=dp_olp_0?ie=UTF8&condition=all&tag=nisa-20&m=ATVPDKIKX0DER",
"XFX Radeon RS RX 480 DirectX 12 ":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814150774",
"XFX Graphic Card RX-480P4JFC6":"https://www.amazon.com/gp/offer-listing/B01M1YE9TD/ref=dp_olp_0?ie=UTF8&condition=all&tag=nisa-20&m=ATVPDKIKX0DER",
"FX Radeon RX 480 DirectX 12 RX480M8BFA6 8GB ":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814150770",
"XFX RADEON RX 480 8GB Custom Tuned OC Graphics Card":"https://www.amazon.com/gp/offer-listing/B01H3P9CKI/?ie=UTF8&condition=all&tag=nisa-20&m=ATVPDKIKX0DER",
"XFX Radeon RX 480 DirectX 12 RX-480M8BBA6 8GB ":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814150772",
"XFX Radeon RX 480 DirectX 12 RX-480M8BBA6 256-bit ":"https://www.amazon.com/gp/offer-listing/B01HOF7ZF6/ref=dp_olp_0?ie=UTF8&condition=all&tag=nisa-20&m=ATVPDKIKX0DER",
"XFX Radeon RX 480 DirectX 12 RX-480M4BFA6 4GB 256-Bit":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814150771",
"VisionTek Radeon RX 480 DirectX 12 900898 8GB":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814129325",
"VisionTek Radeon RX 480 DirectX 12 900888 ":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814129322",
"VisionTek Products Radeon RX 480 8GB GDDR5":"https://www.amazon.com/gp/offer-listing/B01HDUVQZC/ref=dp_olp_0?ie=UTF8&condition=all&tag=nisa-20&m=ATVPDKIKX0DER",
"Sapphire Radeon RX 480 4GB GDDR5 HDMI / TRIPLE DP (UEFI) PCI-Express Graphics Card 21260-01-20G":"https://www.amazon.com/gp/offer-listing/B01HDUVOFO/ref=dp_olp_0?ie=UTF8&condition=all&tag=nisa-20&m=ATVPDKIKX0DER",
"Sapphire Radeon RX 480 8GB GDDR5 HDMI / TRIPLE DP (UEFI) PCI-Express Graphics Card 21260-00-20G":"https://www.amazon.com/gp/offer-listing/B01GTYIEG2/?ie=UTF8&condition=all&tag=nisa-20&m=ATVPDKIKX0DER",
"Sapphire Radeon NITRO+ Rx 480 8GB GDDR5":"https://www.amazon.com/gp/offer-listing/B01J1M4BZ2/ref=dp_olp_0?ie=UTF8&condition=all&tag=nisa-20&m=ATVPDKIKX0DER",
"Sapphire NITRO+ Radeon™ RX 480 4GB GDDR5":"https://www.amazon.com/gp/offer-listing/B01J1M4IHS/ref=dp_olp_0?ie=UTF8&condition=all&tag=nisa-20&m=ATVPDKIKX0DER",
"Sapphire Radeon NITRO+ Rx 480 8GB":"https://www.amazon.com/gp/offer-listing/B01J1M4CZG/ref=dp_olp_0?ie=UTF8&condition=all&tag=nisa-20&m=ATVPDKIKX0DER",
"SAPPHIRE NITRO+ Radeon RX 480 100406NT+8GL 8GB 256-Bit GDDR5 PCI Express 3.0 HDCP Ready Video Card":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814202224",
"SAPPHIRE NITRO+ Radeon RX 480 100406NT+8GOCL 8GB 256-Bit GDDR5 PCI Express 3.0 x16 HDCP Ready Video Card":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814202223",
"SAPPHIRE NITRO+ Radeon RX 480 DirectX 12 100406NT+4GOCL 4GB 256-Bit GDDR5 PCI Express 3.0 x16 HDCP Ready CrossFireX Support Video Card":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814202225",
"SAPPHIRE Radeon RX 480 DirectX 12 100406L 8GB 256-Bit GDDR5 PCI Express 3.0 CrossFireX Support Video Card":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814202221",
"SAPPHIRE Radeon RX 480 100406-4GL 4GB 256-Bit GDDR5 PCI Express 3.0 Video Card":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814202222",
"PowerColor RX 480 Graphic Card (AXRX 480 8GBD5-M3DH)":"https://www.amazon.com/gp/offer-listing/B01HGIQ4R6/ref=dp_olp_0?ie=UTF8&condition=all&tag=nisa-20&m=ATVPDKIKX0DER",
"PowerColor RED DEVIL Radeon RX 480 DirectX 12 AXRX 480 8GBD5-3DHV2/OC ": "https://www.newegg.com/Product/Product.aspx?Item=N82E16814131697",
"PowerColor RED DEVIL Radeon RX 480 DirectX 12 AXRX 480 8GBD5-3DH/OC 8GB":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814131694",
"PowerColor AMD Radeon RED DEVIL RX 480 8GB GDDR5 DL-DVI-D / HDMI / DP x3 PCI-Express 3.0 Graphics Card":"https://www.amazon.com/gp/offer-listing/B01JGQBSV8/ref=dp_olp_0?ie=UTF8&condition=all&tag=nisa-20&m=ATVPDKIKX0DER",
"PowerColor Radeon RX 480 DirectX 12 AXRX 480 4GBD5-M3DH 4GB 256-Bit GDDR5 PCI Express 3.0 ":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814131693",
"PowerColor RED DRAGON Radeon RX 480 DirectX 12 AXRX 480 4GBD5-3DHDV2 4GB 256-Bit GDDR5 PCI Express 3.0 HDCP Ready CrossFireX Support ATX Video Card":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814131706",
"PowerColor RED DRAGON Radeon RX 480 DirectX 12 AXRX 480 4GBD5-3DHD 4GB 256-Bit GDDR5 PCI Express 3.0 ":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814131708",
"MSI GAMING Radeon RX 480 GDDR5 8GB CrossFire VR Ready FinFET DirectX 12 Graphics Card":"https://www.amazon.com/gp/offer-listing/B01K1JTT8S/ref=dp_olp_0?ie=UTF8&condition=all&tag=nisa-20&m=ATVPDKIKX0DER",
"MSI Radeon RX 480 DirectX 12 RX 480 GAMING X 4G 4GB 256-Bit GDDR5 PCI Express 3.0 x16 HDCP Ready CrossFireX Support ATX Video Card":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814137032",
"MSI GAMING Radeon RX 480 GDDR5 4GB CrossFire VR Ready FinFET DirectX 12 Graphics Card (RX 480 GAMING X 4G)":"https://www.amazon.com/gp/offer-listing/B01KIZUF7Y/ref=dp_olp_0?ie=UTF8&condition=all&tag=nisa-20&m=ATVPDKIKX0DER",
"MSI Radeon RX 480 DirectX 12 RX 480 GAMING X 8G 8GB 256-Bit GDDR5 PCI Express 3.0 x16 HDCP Ready CrossFireX Support ATX Video Card":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814137023",
"MSI Radeon RX 480 DirectX 12 RX 480 ARMOR 8G OC 8GB 256-Bit GDDR5 PCI Express 3.0 x16 HDCP Ready CrossFireX Support Video Card":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814137048",
"MSI GAMING Radeon RX 480 GDDR5 8GB CrossFire VR Ready FinFET DirectX 12 Graphics Card":"https://www.amazon.com/gp/offer-listing/B01M4J144F/ref=dp_olp_0?ie=UTF8&condition=all&tag=nisa-20&m=ATVPDKIKX0DER",
"MSI Radeon RX 480 DirectX 12 RX 480 ARMOR 4G OC 4GB 256-Bit GDDR5 PCI Express 3.0 x16 HDCP Ready CrossFireX Support Video Card":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814137049",
"SI GAMING Radeon RX 480 GDDR5 4GB CrossFire VR Ready FinFET DirectX 12 Graphics Card (RX 480 ARMOR 4G OC)":"https://www.amazon.com/gp/offer-listing/B01M368YOU/ref=dp_olp_0?ie=UTF8&condition=all&tag=nisa-20&m=ATVPDKIKX0DER",
"MSI Radeon RX 480 8G":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814127953",
"MSI GAMING Radeon RX 480 GDDR5 HDR VR Ready FinFET DirectX 12 Graphics Card (RX 480 8G)":"https://www.amazon.com/gp/offer-listing/B01GX5Z4EM/ref=dp_olp_0?ie=UTF8&condition=all&tag=nisa-20&m=ATVPDKIKX0DER",
"GIGABYTE Radeon RX 480 DirectX 12 GV-RX480WF2-8GD 8GB 256-Bit GDDR5 PCI Express 3.0 x16 ATX Video Card":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814125912",
"Gigabyte Radeon Rx 480 8GB WINDFORCE GV-RX480WF2-8GD Graphic Cards":"https://www.amazon.com/gp/offer-listing/B01MXDQO8K/ref=dp_olp_0?ie=UTF8&condition=all&tag=nisa-20&m=ATVPDKIKX0DER",
"GIGABYTE Radeon RX 480 DirectX 12 GV-RX480G1 GAMING-8GD 8GB 256-Bit GDDR5 PCI Express 3.0 x16 ATX G1 Gaming 8G Video Card":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814125895",
"Gigabyte Radeon Rx 480 G1 Gaming 8GB GDDR5 Graphics Card (GV-RX480G1 GAMING-8GD)":"https://www.amazon.com/gp/offer-listing/B01KCWZ12W/ref=dp_olp_0?ie=UTF8&condition=all&tag=nisa-20&m=ATVPDKIKX0DER",
"GIGABYTE Radeon RX 480 G1 Gaming 4GB GV-RX480G1GAMING-4GD Video Card":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814125907",
"Gigabyte Radeon Rx 480 G1 Gaming 4GB GDDR5 Graphics Card":"https://www.amazon.com/gp/offer-listing/B01KCWZ1RW/ref=dp_olp_0?ie=UTF8&condition=all&tag=nisa-20&m=ATVPDKIKX0DER",
"GIGABYTE Radeon RX 480 DirectX 12 GV-RX480D5-8GD-B 8GB PCI Express 3.0 x16 ATX Video Card":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814125872",
"DIAMOND Radeon RX 480 DirectX 12 RX480D58G 8GB GDDR5 PCI Express 3.0 x16 CrossFireX Support Video Card":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814103255",
"Diamond Multimedia AMD Radeon Rx 480 PCIe GDDR5 8GB Memory Video Card Graphics Cards RX480D58G":"https://www.amazon.com/gp/offer-listing/B01HTMB89I/?ie=UTF8&condition=all&tag=nisa-20&m=ATVPDKIKX0DER",
"ASUS Radeon RX 480 DirectX 12 DUAL-RX480-O4G 4GB 256-Bit GDDR5 PCI Express 3.0 HDCP Ready CrossFireX Support Video Card":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814126117",
"ASUS ROG STRIX Radeon Rx 480 8GB OC Edition DP 1.4 HDMI 2.0 AMD Polaris Graphics Cards STRIX-RX480-O8G-GAMING":"https://www.amazon.com/gp/offer-listing/B01J3TZJOA/ref=dp_olp_0?ie=UTF8&condition=all&tag=nisa-20&m=ATVPDKIKX0DER",
"ASUS ROG STRIX Radeon Rx 480 8GB DP 1.4 HDMI 2.0 Polaris Vr Ready Graphics Cards":"https://www.amazon.com/gp/offer-listing/B01J3TZMQA/ref=dp_olp_0?ie=UTF8&condition=all&tag=nisa-20&m=ATVPDKIKX0DER",
"ASUS Radeon RX 480 DirectX 12 DUAL-RX480-O4G 4GB 256-Bit GDDR5 PCI Express 3.0 HDCP Ready CrossFireX Support Video Card":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814126108",
"ASUS Radeon RX 480 8GB DisplayPort HDMI AMD Polaris Graphics Card (RX480-8)":"https://www.amazon.com/gp/offer-listing/B01HQB1M2K/?ie=UTF8&condition=all&tag=nisa-20&m=ATVPDKIKX0DER",
"ASUS Radeon RX 480 DirectX 12 DUAL-RX480-O4G 4GB 256-Bit GDDR5 PCI Express 3.0 HDCP Ready CrossFireX Support Video Card":"https://www.newegg.com/Product/Product.aspx?Item=N82E16814126135",
"SUS Dual-Fan Radeon Rx 480 4GB OC Edition AMD Gaming Graphics Card with DP 1.4 HDMI 2.0 (DUAL-RX480-O4G)":"https://www.amazon.com/gp/offer-listing/B01KWGSEJU/ref=dp_olp_0?ie=UTF8&condition=all&tag=nisa-20&m=ATVPDKIKX0DER",
"ASUS Dual-fan Radeon RX 480 4GB AMD Gaming Graphics Card with DP 1.4 HDMI 2.0 (DUAL-RX480-4G)":"https://www.amazon.com/gp/offer-listing/B01LECTVS4/ref=dp_olp_0?ie=UTF8&condition=all&tag=nisa-20&m=ATVPDKIKX0DER"}

	# test
	#url_dict = {"COOLER MASTER R4-S2S-124K-GP Silent Case Fan (4-Pack)":"https://www.newegg.com/Product/Product.aspx?Item=N82E16835103052&cm_re=fan-_-35-103-052-_-Product"}

	limitation = 10

	amount = 0

	f = open("out.txt", "at")


	while True:
		if amount > limitation:
			break
		for key, value in url_dict.items():
			try:
				if amount > limitation:
					break
				browser.visit(value);
				# this is amazon
				if value.find("amazon") != -1:
					print("looking at {0} in Amazon".format(key))
					key_button = browser.find_by_id("oneClickBuyButton")
					if len(key_button) != 0:
						print("IN STOCK!!!!!!!!!!!!!!!!!!!!!!!!!")
						print("{0}: {1} IN STOCK!!!!!!!!!!!!!!!!!!!!!!!!! at AMAZON".format(time.strftime("%Y-%m-%d %H:%M:%S", key, time.localtime()), key), file=f)
						fail = 0
						while True:
							browser.visit(value);
							key_button = browser.find_by_id("oneClickBuyButton")
							if len(key_button) == 0:
								break
							key_button.first.click()
							if browser.is_text_present("Your 1-Click order has been placed"):
								print("Got {0} in Amazon".format(key))
								print("{0}: Got {1} in Amazon".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())), key, file=f)
								amount += 1
							else:
								fail += 1
								print("failed : {0}".format(fail))
								print("{0}: failed {1}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), fail), file=f)
							if fail > 5:
								break
							if amount > limitation:
								break
							
					else:
						print("out of stock")

				# this is in newegg
				elif value.find("newegg") != -1:
					print("looking at {0} in Newegg".format(key))
					#if browser.is_text_present("ADD TO CART"):
					warning = browser.find_by_css("i.fa.fa-exclamation-triangle")
					if len(warning) == 0:
						print("IN STOCK!!!!!!!!!!!!!!!!!!!!!!!!!")
						print("{0}: {1} IN STOCK!!!!!!!!!!!!!!!!!!!!!!!!! at NEWEGG".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), key), file=f)
						fail = 0
						while True:
							# start processing
							# add to cart
							add_cart = browser.find_by_css("button.btn.btn-primary.btn-wide")
							if len(add_cart) != 0:
								add_cart.first.click()
								print("add to cart successfully")
								print("{0}: add to cart successfully".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())), file=f)
							else:
								print("fail to add to cart")
								print("{0}: fail to add to cart".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())), file=f)

							# go to cart
							browser.visit("https://secure.newegg.com/Shopping/ShoppingCart.aspx")

							# got to checkout
							checkout = browser.find_by_css("a.button.button-primary.has-icon-right")
							if len(checkout) != 0:
								#checkout.first.click()
								browser.click_link_by_href("javascript:attachDelegateEvent((function(){Biz.GlobalShopping.ShoppingCart.checkOut('True')}));")
								print("go to checkout successfully")
								print("{0}: go to checkout successfully".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())), file=f)
							else:
								print("fail to checkout")
								print("{0}: fail to checkout".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())), file=f)

							# if need login?
							require_login = browser.find_by_id("submit")
							if len(require_login) != 0:
								#require_login.first.click()
								browser.fill("UserPwd", "12d99mdV!")
								browser.click_link_by_id("submit")
								print("login")
								print("{0}: login".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())), file=f)

							# if quick processing?
							tmp_cvv = browser.find_by_id("cvv2Code")
							tmp_term = browser.find_by_name("AgreeOrNot")
							tmp_place_order = browser.find_by_id("SubmitOrder")
							if len(tmp_cvv) != 0 and len(tmp_term) != 0 and len(tmp_place_order) != 0:
								print("quick order")
								print("{0}: quick order".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())), file=f)
								tmp_cvv.fill("469")
								browser.check("AgreeOrNot")
								browser.click_link_by_href("javascript:Biz.GlobalShopping.CheckOut.submitOrder();")
								print("place order successfully")
								print("{0}: place order successfully".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())), file=f)
								amount += 1
							else:
								print("no quick order")
								print("{0}: no quick order".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())), file=f)
								# no quick processing
								# finish shipping
								shipping = browser.find_by_css("a.button.button-primary.button-override.has-icon-right")
								if len(shipping) != 0:
									#shipping.first.click()
									browser.click_link_by_href("javascript:Biz.GlobalShopping.CheckOut.continueToBilling();")
									print("shipping successfully")
									print("{0}: shipping successfully".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())), file=f)
								else:
									print("fail to shipping")
									print("{0}: fail to shipping".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())), file=f)

								# input cvv
								cvv = browser.find_by_id("creditCardCVV2")
								if len(cvv) != 0:
									cvv.fill("469")
									print("input cvv successfully")
									print("{0}: input cvv successfully".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())), file=f)
								else:
									print("fail to input cvv")
									print("{0}: fail to input cvv".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())), file=f)

								# finish billing
								billing = browser.find_by_css("a.button.button-primary.button-override.has-icon-right")
								if len(billing) != 0:
									browser.click_link_by_href("javascript:Biz.GlobalShopping.CheckOut.continueToReview(1);")
									#billing.first.click()
									print("finish billing successfully")
									print("{0}: finish billing successfully".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())), file=f)
								else:
									print("fail to billing")
									print("{0}: fail to billing".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())), file=f)

								# final term checkbox
								term = browser.find_by_name("AgreeOrNot")
								if len(term) != 0:
									browser.check("AgreeOrNot")
									print("agree term")
									print("{0}: agree term".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())), file=f)
								else:
									print("fail to agree term")
									print("{0}: fail to agree term".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())), file=f)

								# place order
								place_order = browser.find_by_id("SubmitOrder")
								if len(place_order) != 0:
									browser.click_link_by_href("javascript:Biz.GlobalShopping.CheckOut.submitOrder();")
									print("place order successfully")
									print("{0}: place order successfully".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())), file=f)
									amount += 1
								else:
									print("fail to place the order")
									print("{0}: fail to place the order".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())), file=f)
									fail += 1

							if amount > limitation:
								break
							if fail > 5:
								break
							browser.visit(value);
							tmp = browser.find_by_css("i.fa.fa-exclamation-triangle")
							if len(tmp) != 0:
								break

					else:
						print("out of stock")
				f.flush()
			except Exception as e:
				print("{0} type: {1}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), type(e)))    # the exception instance
				print("{0} args: {1}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), e.args))     # arguments stored in .args
				print("{0} e: {1}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), e))

				print("{0} type: {1}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), type(e)), file=f)    # the exception instance
				print("{0} args: {1}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), e.args), file=f)     # arguments stored in .args
				print("{0} e: {1}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), e), file=f)


		