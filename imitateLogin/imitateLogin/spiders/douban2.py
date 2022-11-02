import scrapy


class Douban2Spider(scrapy.Spider):
    name = 'douban2'
    allowed_domains = ['www.douban.com']
    start_urls = ['https://www.douban.com/']

    def parse(self, response):
        yield scrapy.FormRequest.from_response(response,formdata={
            "username":'19558986127',
            "password":'zuozhikun789'
        },callback=self.after_login)


    def after_login(self,response):
        print("111111111111111111111")
        with open('daouban_post.html','w',encoding='utf-8') as f:
            f.write(response.body.decode())
