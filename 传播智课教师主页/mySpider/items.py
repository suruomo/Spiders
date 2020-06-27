# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # 老师姓名
    name = scrapy.Field()
    # 老师职位
    title = scrapy.Field()
    # 老师个人简介
    info = scrapy.Field()
    # pass
