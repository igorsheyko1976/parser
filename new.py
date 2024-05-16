import scrapy


class DivannewlightsSpider(scrapy.Spider):
    name = "divannewlights"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        divans = response.css('div._5FQH')
        for divan in divans:
            yield {
                'name' : divan.css('div.ui-GPFV8 span::text').get(),
                'price' : divan.css('div.tNHiT span::text').get(),
                'url' : divan.css('a').atrib['href']
            }
