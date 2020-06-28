# -*- coding: utf-8 -*-
import scrapy
import json
from douyuSpider.items import DouyuspiderItem


# 抓取斗鱼主播图片保存
class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['douyucdn.cn']
    baseURL = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset="
    # 偏移量
    offset = 0
    start_urls = [baseURL + str(offset)]

    def parse(self, response):
        data_list = json.loads(response.body)['data']
        # 若数据爬完则返回
        if len(data_list) == 0:
            return
        # 开始爬取
        for data in data_list:
            item = DouyuspiderItem()
            item['nickname'] = data['nickname']
            item['imageurl'] = data['vertical_src']
            yield item
        # 修改偏移量，多次爬虫
        self.offset += 20
        yield scrapy.Request(self.baseURL + str(self.offset), callback=self.parse)
