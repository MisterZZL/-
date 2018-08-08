from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

wd = webdriver.Chrome()  # 打开浏览器
wd.get('http://www.baidu.com')  # 输入网址，然后访问

# # 查找元素
kw = wd.find_element_by_id('kw')

# print(str(kw))
# # kw = wd.find_element(By.ID, 'kw')  # 效果同上

# kw.send_keys('动脑')

# # By定位元素的八种方式
# ID # id属性
# XPATH  # xpath
# LINK_TEXT # 链接文本
# PARTIAL_LINK_TEXT# 部分的链接文本
# NAME # name属性
# TAG_NAME # 标签名
# CLASS_NAME # class属性
# CSS_SELECTOR # css选择器

# 定位到元素后，做操作
# wd.find_element(By.ID, "kw").clear()
# wd.find_element(By.ID, "kw").send_keys('动脑学院')
# wd.find_element_by_xpath("//*[@id='su']").click()

# 点击百度页面的 登陆
# wd.find_element_by_xpath("//*[@id='u1']/a[7]").click()
