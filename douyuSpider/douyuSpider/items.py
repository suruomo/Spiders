# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class DouyuspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # 昵称
    nickname=scrapy.Field()
    # 图片链接
    imageurl=scrapy.Field()
