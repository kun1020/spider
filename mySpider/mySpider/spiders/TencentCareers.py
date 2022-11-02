import json
import scrapy
class TencentcareersSpider(scrapy.Spider):
    name = 'TencentCareers'
    allowed_domains = ['careers.tencent.com']
    start_urls = ["https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1666011232363&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex=1&pageSize=10&language=zh-cn&area=cn"]

    def parse(self, response):
        pageIndex = int(response.url.split('&')[9].split('=')[1])
        print(pageIndex)

        data = response.body.decode('utf-8')
        data_dict = json.loads(data)
        data_list = data_dict["Data"]["Posts"]

        for data in data_list:
            di = {}
            di['name'] = data["RecruitPostName"]
            di['PostURL'] = data["PostURL"]
            di['Responsibility'] = data["Responsibility"].replace('\n','')
            di['PostId'] = data['PostId']
            # print('+' * 100)
            # print(di)
            # print('+' * 100)

            url_in = f"https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1666019833558&postId={di['PostId']}&language=zh-cn"
            yield scrapy.Request(url=url_in,callback=self.parse_next,meta=di)

        # if len(data_list) < 10:
        #     pass
        # else:
        #     next_url = f"https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1666011232363&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex={pageIndex+1}&pageSize=10&language=zh-cn&area=cn"
        #     yield scrapy.Request(url=next_url,callback=self.parse)


    def parse_next(self,response):
        di =  response.meta
        data = response.body.decode('utf-8')
        data_dict = json.loads(data)
        di['duty'] = data_dict['Data']['Responsibility'].replace('\n','')
        di['Requirement'] = data_dict['Data']['Requirement'].replace('\n','')
        # print('*'*100)
        # print(di)
        # print('*' * 100)
        yield di