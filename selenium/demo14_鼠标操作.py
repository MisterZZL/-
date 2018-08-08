# coding=utf-8
# author:dn_eric(qq:2384363842)
# 动脑学院pythonVip课程
# 创建于: 2018/1/31 14:58

"""
在 WebDriver 中， 将这些关于鼠标操作的方法封装在 ActionChains 类提供。
ActionChains 类提供了鼠标操作的常用方法：
perform()： 执行所有 ActionChains 中存储的行为；
context_click()： 右击；
double_click()： 双击；
drag_and_drop()： 拖动；
move_to_element()： 鼠标悬停。
drag_and_drop_by_offset(): 拖拽
"""
import time
from selenium import webdriver
# 引入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.baidu.cn")

# 定位到要悬停的元素
above = driver.find_element_by_link_text("设置")
# 对定位到的元素执行鼠标悬停操作
ActionChains(driver).move_to_element(above).perform()
time.sleep(3)

ActionChains(driver).context_click(above).perform()
