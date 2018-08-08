'''
    requests-html是大神kennethreitz新写的包，用于爬虫与解析HTML,很好用
    安装: pip install requests-html
    github: https://github.com/kennethreitz/requests-html

    先理解页面加载的两种方式，直接加载，ajax异步请求加载修改DOM
'''
import time
from pyppeteer import chromium_downloader
from requests_html import HTMLSession

session = HTMLSession()  # 继承自 requests.Session

# # 1.常规使用
# r = session.get('https://python.org/')
# print(r)  # Response 对象
# print(r.html)  # HTML对象
# print(r.html.html)  # html文本内容
#
title = r.html.find('title', first=True)  # 如果不加first=True返回的是列表，哪怕只有一个标签元素
# print(title)
# print(title.text)
# print(title.html)
#
# about = r.html.find('#about', first=True)  # 根据CSS选择器查找元素
# print(about.text)
# print(about.html)
# print(about.attrs)


# # 2. 支持css选择器与xpath选择器
# r = session.get('https://www.baidu.com/')
# # css选择器
# print(r.html.find('#su', first=True).attrs['value'])
# # xpath选择器
# print(r.html.xpath('//*[@id="su"]')[0].attrs['value'])


# # 3.检索
# result = r.html.search('Python is a {} language')[0]
# print(result)


## 4.不使用Requests，单独使用解析部分
# from requests_html import HTML
#
# doc = """<a href='https://python.org/'>python官网</a>"""
#
# html = HTML(html=doc)
# print(html.links)
# print(html.find('a', first=True).text)


# 其实requests_html还存在一些问题，比如render方法就存在问题，就不演示了。
# 但大家要理解软件有问题是正常的，就像python本身也是存在bug，也需要大家提issues。
# 发现bug可以提issues，有余力的软件爱好者都可以修复bug。
# 做出自己的贡献,能做到这一点，也是以后职业生涯的亮点。
# 想到自己写的代码被无数次的使用，也是开心的事情。
