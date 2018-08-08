from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

wd = webdriver.Chrome()  # 打开浏览器
wd.get('http://www.baidu.com')  # 输入网址，然后访问

# 等待，三种方式
# # 1.强制等待
# import time
# time.sleep(5)
# kw = wd.find_element_by_id('kw')  # 查找元素

# # 2.隐式等待
# implicitly_wait()默认参数的单位为秒，本例中设置等待时长为10秒。
# 首先这10秒并非一个固定的等待时间，它并不影响脚本的执行速度。
# 其次，它并不针对页面上的某一元素进行等待。当脚本执行到某个元素定位时，如果元素可以定位，则继续执行；
# 如果元素定位不到，则它将以轮询的方式不断地判断元素是否被定位到。
# 假设在第6秒定位到了元素则继续执行，若直到超出设置时长（10秒）还没有定位到元素，则抛出异常

# 总结特点如下
# a.全局有效
# b.等待时间内如10s之后还找不到（可能没有也可能没加载出来）则抛出未找到元素的异常
# c.如果在时间内，找到了，就不会等下去
wd.implicitly_wait(10)
kw = wd.find_element_by_id('kw')  # 查找元素
kw = wd.find_element(By.ID, 'kw')
kw.send_keys('动脑学院')  # 填充表单输入框内容

# # 3.显式等待
# WebDriverWait类是由WebDirver 提供的等待方法。
# 在设置时间内，默认每隔一段时间检测一次当前页面元素是否存在，
# 如果超过设置时间检测不到则抛出异常

# 总结特点如下
# a.特定使用才生效
# b.等待时间内如10s之后还找不到（可能没有也可能没加载出来）则抛出未找到元素的异常
# c.如果在时间内，找到了，就不会等下去

wait = WebDriverWait(wd, 10)  # 还有第三个参数 poll_frequency，多久检测一次元素是否存在了
kw = wait.until(expected_conditions.presence_of_element_located((By.ID, 'kw')))
