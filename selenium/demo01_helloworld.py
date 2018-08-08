from selenium import webdriver
from selenium.webdriver.common.by import By

# 1.hello,world
# 对应浏览器驱动
dw = webdriver.Chrome()  # executable_path="chromedriver"
# dw.get("https://www.baidu.com")
# # dw.get("http://127.0.0.1:8080/ajax_loader")
# print(dw.title)
# print(dw.page_source)  # page_source获取网页html(dom操作处理后的)

# 2.设置浏览器窗口大小
# dw.set_window_size(400, 800)
# dw.maximize_window()
# dw.minimize_window()

# 3.控制浏览器后退、前进
# 在使用浏览器浏览网页时，浏览器提供了后退和前进按钮，可以方便地在浏览过的网页之间切换，
# WebDriver也提供了对应的back()和forward()方法来模拟后退和前进按钮。

first_url = "https://www.baidu.com"
print("访问%s" % (first_url))
dw.get(first_url)

second_url = "http://news.baidu.com"
print("访问%s" % (second_url))
dw.get(second_url)
#
#
dw.back() # 后退
print(dw.current_url)
#
dw.forward() # 前进
print(dw.current_url)
#
# 4.关闭整个浏览器，所有打开的窗口都关掉并且退出webdirver
dw.quit()
