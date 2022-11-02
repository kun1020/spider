import scrapy

class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['douyu.com']
    start_urls = ['https://www.douyu.com/']

    def parse(self, response):
        print('*'*100)
        print('1111111111111111111')
        print(response)
        print('*'*100)



