# -*- coding: utf-8 -*-
__author__ = 'suruomo'
__date__ = '2020/6/29 13:44'

from selenium.webdriver import Chrome, ChromeOptions
import json

# 获取陕西政务平台审批项目数据
# 动态网页，使用browser.page_source获取渲染后的网站源码
# 翻页在js中，需要selenium操作浏览器获取
base_url = "http://tzxm.shaanxi.gov.cn/tzxmweb/pages/home/approvalResult/queryPublicResultNew.jsp"
option = ChromeOptions()
option.add_argument("--headless")  # 隐藏游览器
option.add_argument("--no--sandbox")
browser = Chrome(options=option, executable_path="D:\\Notebook\\chromedriver.exe")

data = []  # 存储数据

browser.get(base_url)
html = browser.page_source
# 翻页爬取数据
for page in range(1,11):
    print("第"+str(page)+"页爬虫\n")
    # 翻页后需要重新定位元素
    content = browser.find_elements_by_xpath('//*[@id="tablist"]/tr')
    # 从list[2]数据开始爬取，每隔两个元素获取数据，直到全部结束
    for c in content[2::3]:
        name = c.find_element_by_xpath("./td[1]").text
        department = c.find_element_by_xpath("./td[2]").text
        status = c.find_element_by_xpath("./td[3]").text
        date = c.find_element_by_xpath("./td[last()]").text
        data.append({"name": name, "department": department, "status": status,
                     "date": date})
        # 点击下一页继续爬取数据
    button=browser.find_element_by_xpath('//*[@id="pageBox"]/div[2]/a[4]').click()
# 关闭浏览器
browser.close()
# 字典转为json
json_str = json.dumps(data, indent=4, ensure_ascii=False)
# 写入文件
with open("data.json", "w+", encoding='utf-8') as f:
    f.write(json_str)
    f.write('\n')
