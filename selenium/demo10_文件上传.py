import time
import os

from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(60)
driver.get("http://www.layui.com/demo/upload.html")
# 定位上传按钮，添加本地文件
basedir = os.path.dirname(__file__)
filename = os.path.join(basedir, 'img', 'logo.jpg')
driver.find_element_by_name("file").send_keys(filename)

time.sleep(20)
driver.quit()
