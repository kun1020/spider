import scrapy

class doubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://www.douban.com/']
    cookies = "ll=118226; bid=0MatAuGUit8; __gads=ID=9f9a47265f671146-22c7f560e4d6005c:T=1665107102:RT=1665107102:S=ALNI_MaZVeLDixMTmUQaFeCl4PsD029EgA; push_noty_num=0; push_doumail_num=0; _ga=GA1.2.938883266.1665106929; ct=y; gr_user_id=47231423-abd3-44ec-80ce-00b2c6dc3627; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1666403871%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DDhMpLjv6J3t2eaS5FS54yV3yoO9Y7WM5wTQiYJwP2ewuwDo-4MiCzVpiPLMcl6Tn%26wd%3D%26eqid%3De185bd8400013d300000000363534e19%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.938883266.1665106929.1666332836.1666403872.7; __utmc=30149280; __utmz=30149280.1666403872.7.7.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; ap_v=0,6.0; __utmv=30149280.26344; __yadk_uid=pu8gPf0Xp6Edy5oznDmKp6nfHrmC56PJ; __gpi=UID=00000a1fea741ec0:T=1665107102:RT=1666403920:S=ALNI_MZbuDgtlfAMAA37jOjez88k2QeThA; dbcl2=263444075:ryeSiJcyVh0; ck=-Gp9; _pk_id.100001.8cb4=edfd3b0d33eba3f4.1665106928.5.1666403999.1666319767.; __utmb=30149280.11.10.1666403872"
    cookies_dict = {item.split('=')[0]:item.split('=')[1] for item in cookies.split(";")}
    # headers = {
    #     "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    #     "referer":"https://graph.qq.com/"
    # }

    def start_requests(self):
        # yield scrapy.Request(self.start_urls[0],callback=self.parse,cookies=self.cookies_dict,headers=self.headers)
        yield scrapy.Request(self.start_urls[0],callback=self.parse,cookies=self.cookies_dict)

    def parse(self, response):
        print('*' * 100)
        print(response)
        print(self.cookies_dict)
        print('*' * 100)
        with open('douban.html', 'w', encoding='utf-8') as f:
            f.write(response.body.decode())
        # url = "https://www.douban.com/people/263444075/?_i=64044380MatAuG"
        # yield scrapy.Request(url,callback=self.parse_prople)
