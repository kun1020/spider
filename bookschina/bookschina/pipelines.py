# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json

from itemadapter import ItemAdapter

class BookschinaPipeline:
    def open_spider(self,spider):
        self.f = open('bookschina.txt','w',encoding='utf-8')

    def process_item(self, item, spider):
        json.dump(item,self.f,ensure_ascii=False,indent=4)

    def close_spider(self,spider):
        self.f.close()
