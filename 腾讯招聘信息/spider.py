# -*- coding: utf-8 -*-
__author__ = 'suruomo'
__date__ = '2020/6/27 19:37'

from selenium.webdriver import Chrome, ChromeOptions
import json

# 爬取腾讯招聘网站
# 动态网页，使用browser.page_source获取渲染后的网站源码
base_url = "https://careers.tencent.com/search.html?index="
option = ChromeOptions()
option.add_argument("--headless")  # 隐藏游览器
option.add_argument("--no--sandbox")
browser = Chrome(options=option, executable_path="D:\\Notebook\\chromedriver.exe")

data = []  # 存储数据
# 翻页爬取数据
for page in range(1, 11):
    url = base_url + str(page)
    browser.get(url)
    html = browser.page_source
    content = browser.find_elements_by_xpath("//*[@class='recruit-list-link']")
    for c in content:
        name = c.find_element_by_xpath("./h4").text
        company = c.find_element_by_xpath("./p[1]/span[1]").text
        workLocation = c.find_element_by_xpath("./p[1]/span[2]").text
        classification = c.find_element_by_xpath("./p[1]/span[position()>2 and position()<last()]").text
        publishTime = c.find_element_by_xpath("./p[1]/span[last()]").text
        detailInfo = c.find_element_by_xpath("./p[2]").text
        data.append({"name": name, "company": company, "workLocation": workLocation,
                     "classification": classification, "publishTime": publishTime, "detailInfo": detailInfo})
# 关闭浏览器
browser.close()
# 字典转为json
json_str = json.dumps(data, indent=4, ensure_ascii=False)
# 写入文件
with open("data.json", "w+", encoding='utf-8') as f:
    f.write(json_str)
    f.write('\n')
