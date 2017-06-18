from scrapy.selector import Selector
from scrapy import Spider
from nowinstock_scraper.items import NowinstockScraperItem

class NowinStock_spider(Spider):
    name = "nowinstock_spider"
    allowed_domains = ["nowinstock.net"]
    start_url = ["http://www.nowinstock.net/computers/videocards/amd/rx570/"]
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    def parse(self, response):
        print(response)
        sel = Selector(response)
        sites = sel.xpath('//tr/td')
        item = NowinstockScraperItem
        items = []
        for site in sites:
            item['name'] = site.xpath('a/text()').extract()
            item['link'] = site.xpath('a/@href').extract()
            items.append(item)

        return items
        # sel.xpath('//tr/td/a/text()').extract()
        # sel.xpath('//tr/td/a/@href').extract()



