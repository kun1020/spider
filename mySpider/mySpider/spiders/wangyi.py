import scrapy
import logging

class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    allowed_domains = ['music.163.com']
    start_urls = ['http://music.163.com/']

    def parse(self, response):
        di = {'name':'zuozhikun'}
        return di
