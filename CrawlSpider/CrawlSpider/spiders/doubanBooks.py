import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class DoubanbooksSpider(CrawlSpider):
    name = 'doubanBooks'
    allowed_domains = ['book.douban.com']
    start_urls = ["https://book.douban.com/tag/?view=type&icn=index-sorttags-all"]

    rules = (
        Rule(LinkExtractor(allow=r"tag/(\w+)|[\\u4e00-\\u9fa5]$"),follow=True),
        Rule(LinkExtractor(allow=r"https://book.douban.com/subject/(\d+)/"),callback='parse_item',follow=True)
    )

    def parse_item(self, response):
        book = {}
        book['title'] = response.xpath("//div[@id='wrapper']/h1/span/text()").extract_first()
        book['publisher'] = response.xpath("//div[@id='info']/a[1]/text()").extract_first()
        book['price'] = response.xpath("//div[@id='info']/span[3]/following::text()[21]")
        yield book

