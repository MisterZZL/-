"""
在Web应用中经常会遇到frame/iframe表单嵌套页面的应用，
WebDriver只能在一个页面上对元素识别与定位，
对于frame/iframe表单内嵌页面上的元素无法直接定位。
这时就需要通过switch_to.frame()方法将当前定位的主体切换为frame/iframe表单的内嵌页面中。
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(60)
driver.get("https://mail.126.com/")
fr = driver.find_element_by_id('x-URS-iframe')
driver.switch_to.frame(fr)
import time

time.sleep(3)
element = WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.NAME, "email")))
driver.find_element_by_name("email").clear()
driver.find_element_by_name("email").send_keys("username")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("password")
driver.find_element_by_id("dologin").click()
driver.switch_to.default_content()
import time

time.sleep(5)
driver.quit()

# xf = driver.find_element_by_xpath('//*[@id="x-URS-iframe"]')
# driver.switch_to.frame(xf)

# switch_to.frame() 默认可以直接取表单的id 或name属性。
# 如果iframe没有可用的id和name属性，则可以通过下面的方式进行定位。
# 除此之外，在进入多级表单的情况下，还可以通过switch_to.default_content()跳回最外层的页面
