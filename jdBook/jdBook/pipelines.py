# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json


class JdbookPipeline:
    def __init__(self):
        self.f = open("data/book.json", "wb+")

    def process_item(self, item, spider):
        content = json.dumps(dict(item), indent=4,ensure_ascii=False)+",\n"
        self.f.write(content.encode("utf-8"))
        return item

    def close_spider(self, spider):
        self.f.close()
