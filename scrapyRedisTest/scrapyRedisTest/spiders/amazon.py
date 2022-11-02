import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider

class AmazonSpider(RedisCrawlSpider):
    name = 'amazon'
    redis_key = 'amazon'
    allowed_domains = ['amazon.cn']
    # start_urls = ['http://amazon.cn/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=("//div[@id='s-refinements']/div/div/ul/li/span/a")),follow=True),
        Rule(LinkExtractor(restrict_xpaths=("//div[@class='a-section a-text-center s-pagination-container']/span/a[last()]")),follow=True),
        Rule(LinkExtractor(restrict_xpaths=("//div[@class='sg-col sg-col-4-of-12 sg-col-8-of-16 sg-col-12-of-20 s-list-col-right']/div/div/div/h2/a")),callback='parse_item',follow=False)
    )

    def parse_item(self, response):
        item = {}
        item['first_lable'] = response.xpath("//ul[@class='a-unordered-list a-horizontal a-size-small']/li[1]/span/a/text()").extract_first()
        item['second_lable'] = response.xpath("//ul[@class='a-unordered-list a-horizontal a-size-small']/li[3]/span/a/text()").extract_first()
        item['title'] = response.xpath("//span[@id='productTitle']/text()").extract_first()
        item['author'] = response.xpath("//div[@id='bylineInfo']/span[1]/a/text()").extract_first()
        print(item)

        return item

