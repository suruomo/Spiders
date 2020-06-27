# -*- coding: utf-8 -*-
import scrapy


class XicidailiSpider(scrapy.Spider):
    name = 'xicidaili'  # 必须唯一
    allowed_domains = ['xicidaili.com']  # 允许采集域名

    # start_urls = [f'https://www.xicidaili.com/nn/{page}'for page in range(1,3685)]  # 开始网站
    start_urls = ['https://www.xicidaili.com/nn/3']  # 开始网站

    # 解析响应数据 提取数据或者网址等等
    def parse(self, response):
        selectors = response.xpath('//tr')
        for selector in selectors:
            ip = selector.xpath('./td[2]/text()').get()
            port = selector.xpath('./td[3]/text()').get()
            print(ip,port)


        # 翻页操作
        # next_page=response.xpath('//a[@class="next_page"]/@href').get()
        # if next_page:
        #     print(next_page)
        #     # 拼接网址
        #     next_url=response.urljoin(next_page)
        #     # 发出请求
        #     yield scrapy.Request(next_url,callback=self.parse)
