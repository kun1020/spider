import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider

class SobooksSpider(RedisCrawlSpider):
    name = 'sobooks'
    allowed_domains = ['sobooks.net']
    redis_key = "sobooks:url"
    # start_urls = ['http://sobooks.net/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=("//div[@id='nav-header']/ul/li/a")), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        print("1111111111111111111111")
        print(response.url)
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
