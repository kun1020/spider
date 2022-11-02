import re
import scrapy
from scrapy_redis.spiders import RedisSpider

class ChaoxingSpider(RedisSpider):
    name = 'chaoxing_redis'
    redis_key = "chaoxing_start_urls"
    allowed_domains = ['book.chaoxing.com']
    # start_urls = ['http://book.chaoxing.com/']

    def parse(self, response):
        # li_list = response.xpath("//div[@class='All']/ul[@class='All_list']/li")
        li_list = []
        li = response.xpath("//div[@class='All']/ul[@class='All_list']/li[3]")
        li_list.append(li)
        for li in li_list:
            item = {}
            item['total_type'] = li.xpath("./a/text()").extract_first()
            a_list = li.xpath("./div/a")
            for a in a_list:
                item['title'] = a.xpath("./text()").extract_first()
                a_href = a.xpath("./@href").extract_first()
                url = "http://book.chaoxing.com" + a_href
                yield scrapy.Request(url, callback=self.parse_detail, meta=item)

    def parse_detail(self,response):
        item = response.meta
        li_list = response.xpath("//ul[@class='list']/li")
        for li in li_list:
            item['book_name'] = li.xpath("./div[2]/div/p/a/text()").extract_first()
            item['author'] = li.xpath("./div[2]/p[1]/span").extract_first()
            a_href = li.xpath("./div[2]/div/p/a/@href").extract_first()
            url = "http://book.chaoxing.com" + a_href
            yield scrapy.Request(url,callback=self.parse_book_detail,meta=item)

        # 翻页模块
        ret = re.search(r'/nPage_(\d+)/size', response.url)
        current_page = ret.group(1)
        end_page_url = response.xpath("//div[@id='pager']/a[@v='last']/@href").extract_first()
        if end_page_url is None:
            pass
        else:
            ret1 = re.search(r'/nPage_(\d+)/size', end_page_url)
            end_page = ret1.group(1)
            if current_page != end_page:
                url = f"http://book.chaoxing.com/search/keyword_/fenleiID_1401/field_01/sortName_/nPage_{int(current_page)+1}/size_10.html"
                print(url)
                yield scrapy.Request(url,callback=self.parse_detail,meta=item)

    def parse_book_detail(self,response):
        item = response.meta
        li_list = response.xpath("//div[@class='list clearfix']/ul[1]")
        for li in li_list:
            item['出版日期']=li.xpath("./li[2]/text()").extract_first()
            item['出版社']=li.xpath("./li[3]/text()").extract_first()
        yield item

        '''
            {'total_type': '马克思主义、列...', 'title': '马克思、恩格斯...', 'depth': 2, 'download_timeout': 180.0,
             'download_slot': 'book.chaoxing.com', 'download_latency': 0.17399978637695312,
             'book_name': '马克思  哲学的贫困', 'author': ' < span > 马克思 Marx < / span > '}
        '''
