# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json

from itemadapter import ItemAdapter

class MyspiderPipeline:
    # def process_item(self, item, spider):
    #     # total_list = []
    #     # total_list.append(item)
    #     with open('tencent.txt','a',encoding='utf-8') as f:
    #         json.dump(item,f,ensure_ascii=False,indent=4)
    #     return item
    def process_item(self, item, spider):
        print(item['name'])
        return item
