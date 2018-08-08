# coding=utf-8
# author:dn_eric(qq:2384363842)
# 动脑学院pythonVip课程
# 创建于: 2018/1/31 15:17
"""
Keys()类提供了键盘上几乎所有按键的方法。 前面了解到， send_keys()方法可以用来模拟键盘输入，
除此 之外， 我们还可以用它来输入键盘上的按键， 甚至是组合键， 如 Ctrl+A、 Ctrl+C 等。
"""
import time
from selenium import webdriver
# 引入 Keys 模块
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

# 输入框输入内容
driver.find_element_by_id("kw").send_keys("动脑学员")
time.sleep(3)
# 删除输入错误的一个员
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
time.sleep(3)

# 输入“院”
driver.find_element_by_id("kw").send_keys("院")
time.sleep(3)
# ctrl+a 全选输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')
time.sleep(3)
# ctrl+x 剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')

# ctrl+v 粘贴内容到输入框
time.sleep(3)
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'v')
# 通过回车键来代替单击操作
driver.find_element_by_id("su").send_keys(Keys.ENTER)
time.sleep(3)
driver.quit()