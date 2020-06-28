# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from douyuSpider.settings import IMAGES_STORE
from scrapy.pipelines.images import ImagesPipeline
import os

# 使用图片管道
class DouyuspiderPipeline(ImagesPipeline):

    # 获取图片
    def get_media_requests(self, item, info):
        image_link = item['imageurl']
        yield scrapy.Request(image_link)

    # 获取后处理：重命名
    # results中提取本地保存path，修改
    def item_completed(self, results, item, info):
        # 取出路径
        image_url=[x["path"] for ok,x in results if ok]
        # 重命名
        os.rename(IMAGES_STORE+image_url[0],IMAGES_STORE+item['nickname']+".jpg")
        return item
