import os
from selenium import webdriver

dr = webdriver.Chrome()
dr.get("http://www.baidu.com")

os.makedirs('output', exist_ok=True)
file_name_ss = 'output/截图.png'
dr.get_screenshot_as_file(file_name_ss)
dr.quit()
