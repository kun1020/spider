import time

import scrapy


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['www.bookschina.com']
    start_urls = ['http://www.bookschina.com/books/kinder/']

    def parse(self, response):
        a_list = response.xpath("//div[@class='w1200 clearfix']/ul[1]/li/a")
        # print(a_list)
        for a in a_list:
            # extract_first() 取每个对象中的数据的第一个内容
            item = {}
            item["tags"] = a.xpath("text()").extract_first()
            href = a.xpath("@href").extract_first()
            url = "http://www.bookschina.com" + href
            # url = "http://www.bookschina.com/kinder/53110000/"
            # print(url)
            time.sleep(1)
            yield scrapy.Request(url,callback=self.parse_list,meta=item)

    def parse_list(self,response):
        item = response.meta
        a_list = response.xpath("//div[@class='bookList']/ul/li/div[2]/h2/a")
        for a in a_list:
            item['book_title'] = a.xpath("text()").extract_first()
            href = a.xpath("@href").extract_first()
            url = "http://www.bookschina.com" + href
            yield scrapy.Request(url, callback=self.parse_detail, meta=item)

    def parse_detail(self,response):
        item = response.meta
        price = response.xpath("//div[@class='priceWrap']/span[2]/text()").extract_first()
        item['price'] = price
        print(item)
        yield item