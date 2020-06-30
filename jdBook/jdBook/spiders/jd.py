# -*- coding: utf-8 -*-
from copy import deepcopy

import scrapy

from jdBook.items import JdbookItem


class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com']
    start_urls = ['https://book.jd.com/booksort.html']

    def parse(self, response):
        dt_list = response.xpath('//*[@id="booksort"]/div[2]/dl/dt')  # 大标签列表
        for dt in dt_list:
            item=JdbookItem()
            b_cate = dt.xpath('./a/text()').extract_first()
            dd_list = dt.xpath('./following-sibling::dd[1]/em')  # 小标签列表
            for dd in dd_list:
                item['b_cate'] = b_cate
                item['s_cate'] = dd.xpath('./a/text()').extract_first()  # 小标签名称
                item['s_cate_url'] = dd.xpath('./a/@href').extract_first()  # 小标签地址
                # yield item
                # 如果小标签不为空
                if item['s_cate_url'] is not None:
                    # 补全地址
                    item['s_cate_url'] = "https:" + item['s_cate_url']
                    yield scrapy.Request(item['s_cate_url'],
                            callback=self.parse_book_list,
                            meta={"item": deepcopy(item)})

    # 解析每一类别下书籍详细信息
    def parse_book_list(self, response):
        item=response.meta['item']
        li_list=response.xpath('//*[@id="J_goodsList"]/ul/li')  # 书籍列表
        for li in li_list:
            item['book_img']="https:"+li.xpath('./div/div[1]/a/img/@src').extract_first()
            item['book_name']=li.xpath('./div/div[3]/a/em/text()').extract_first()
            item['book_author']=li.xpath('./div/div[4]/span[1]/a/text()').extract_first()
            item['book_press']=li.xpath('./div/div[4]/span[2]/a/text()').extract_first()  # 出版社
            item['book_publish_date']=li.xpath('./div/div[4]/span[3]/text()').extract_first()
            item['book_price']=li.xpath('./div/div[2]/strong/i/text()').extract_first()
            yield item





