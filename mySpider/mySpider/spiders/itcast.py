# -*- coding: utf-8 -*-
import scrapy

from mySpider.items import MyspiderItem


# 爬取传智播客的老师信息

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        node_list = response.xpath("//div[@class='li_txt']")

        items = []
        for node in node_list:
            item = MyspiderItem()

            name = node.xpath("./h3/text()").extract()
            title = node.xpath("./h4/text()").extract()
            info = node.xpath("./p/text()").extract()

            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]
            # 返回提取到的每一个item数据，交给管道文件处理，同时回来继续执行后面的代码
            yield item

