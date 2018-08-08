# Beautiful soup 从html 或xml文件中提取数据的python库
# 安装 pip install bs4  或者 pip install beautifulsoup4
# 官方文档 http://beautifulsoup.readthedocs.io/zh_CN/latest/

# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>
#
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
#
# <p class="story">...</p>
# """
#
# from bs4 import BeautifulSoup
#
# '''
#     使用BeautifulSoup解析这段代码,能够得到一个 BeautifulSoup 的对象,并能按照标准的缩进格式的结构输出:
# '''
# soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.prettify()) # 标准格式输出

# # 几个简单的浏览结构化数据的方法
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.p)
# print(soup.p['class'])
# print(soup.a)
# print(soup.find_all('a'))
# print(soup.find(id="link3"))

# # 从文档中找到所有<a>标签的链接
# for link in soup.find_all('a'):
#     print(link.get('href'))

# # 从文档中获取所有文字内容:
# print(soup.get_text())


'''
    Beautiful Soup支持Python标准库中的HTML解析器,还支持一些第三方的解析器。
    支持的解析器有：
    
    html.parse  python内置标准库，速度适中
    lxml html解析器,使用xpath技术局部遍历速度会快一些
    lxml xml 速度快 文档容错能力强
    html5lib 速度慢，以浏览器方式解析文档
    
    推荐使用lxml作为解析器,因为效率更高,lxml是第三方的解析器所以需要安装
    安装: pip install lxml
    
    更详细的内容可以看官方文档：http://beautifulsoup.readthedocs.io/zh_CN/latest/
'''

from bs4 import BeautifulSoup

# # 可以传入一段字符串或一个文件句柄构造 BeautifulSoup.
# soup = BeautifulSoup(open("demo02.html"), 'lxml')
# print(soup)
# soup = BeautifulSoup("<html>data</html>", 'lxml')
# print(soup)

'''
Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,
所有对象可以归纳为4种: Tag(标签) , NavigableString（标签内容）, BeautifulSoup(文档全部内容), Comment（注释）
'''

# # 1.Tag(标签)
soup = BeautifulSoup('<b class="boldest" >Extremely bold</b>', 'lxml')
tag = soup.b
# print(type(tag))
# print(tag)

# tag中最重要的属性: name(标签名称)和attributes(属性)
# name
# print(tag.name)
# tag.name = 'blockquote'
# print(tag.name)         # b
# print(tag)
#
# # attributes 属性
# '''
#     一个tag可能有很多个属性. tag <b class="boldest"> 有一个 “class” 的属性,值为 “boldest”
#      tag的属性的操作方法与字典相同:
# '''
# print(tag['class'])
# print(tag.attrs)
#
# # 多值属性
# css_soup = BeautifulSoup('<p id="my id" class="body strikeout"></p>', 'lxml')
# print(css_soup.p['class'])
# print(css_soup.p['id'])  # 在HTML定义中id没有被定义为多值属性


# # 2.NavigableString 继承自str
from bs4.element import NavigableString
# soup = BeautifulSoup('<title>Hello,World</title>', 'lxml')
# tag = soup.title
# print(type(tag.string))         #<class 'bs4.element.NavigableString'>
# print(tag.string)           #Hello,World


# # 3.BeautifulSoup 该对象表示的是一个文档的全部内容，大部分时候,可以把它当作 Tag 对象
# # 因为 BeautifulSoup 对象并不是真正的HTML或XML的tag,所以它没有name和attribute属性
# # 但包含了一个值为 “[document]” 的特殊属性 .name
#
# soup = BeautifulSoup('<title>Hello,World</title>', 'lxml')
# print(soup)             #<html><head><title>Hello,World</title></head></html>
# print(type(soup))       #<class 'bs4.BeautifulSoup'>
# print(soup.name)        #[document]


# # 4.Comment 注释，最终也是继承自str
# from bs4.element import Comment
# markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
# soup = BeautifulSoup(markup, 'lxml')
# comment = soup.b.string
# print(type(comment))
# print(comment)

# Beautiful Soup定义了很多搜索方法,这里着重介绍2个: find() 和 find_all()
# 查找元素 find 单个标签 find_all 标签列表
# 默认是根据name来搜索，也可以用其他属性来搜索,
# 搜索指定名字的属性时可以用参数值包括 字符串，正则表达式、列表、True
import re

soup = BeautifulSoup(open('demo02.html'), 'html.parser')

# print(soup.find_all(class_='sister'))
# print(soup.find_all(class_=['sister', 'sister1']))
# print(soup.find_all(href=re.compile("http://example.com/")))

# text 查找文档内容参数，limit 限制个数参数、recursive递归参数
# print(soup.find_all(text='Elsie', limit=1, recursive=True))
# print(soup.find_all(text=['Elsie', 'Lacie'], limit=5, recursive=True))
#
# a_list = soup.find_all('a', attrs={"id": "link1"}, )
# for item in a_list:
#     print(item)

# css 选择
# 使用浏览器开发者工具 直接看浏览器copy as css

# # css类名前加. id前加#
# # 使用标签名称查找：
# a_list = soup.select("a", limit=3)  # 返回list
# print(a_list)
# title = soup.select("html title")
# print(title)
#
# # > 直接子元素，以下代码查找不到
title = soup.select("html > title")
print(title)

print(soup.select('.sister'))
print(soup.select('a#link3'))
#
# # # 存在某属性的标签
# print(soup.select('a[class]'))
# print(soup.select('a[href="http://example.com/elsie"]'))
