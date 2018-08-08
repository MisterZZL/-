from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(60)
driver.get("http://www.baidu.com")

# 获得百度搜索窗口句柄
sreach_windows = driver.current_window_handle

driver.find_element_by_link_text('登录').click()
driver.find_element_by_link_text("立即注册").click()

# 获得当前所有打开的窗口的句柄
all_handles = driver.window_handles

# 进入注册句柄
for handle in all_handles:
    if handle != sreach_windows:
        driver.switch_to.window(handle)  # 切换句柄
        print('now register window!')
        driver.find_element_by_name("userName").send_keys('dongnaoedu_110')
        driver.find_eleqment_by_name('phone').send_keys('13008909898')
        driver.find_element_by_id('TANGRAM__PSP_3__password').send_keys("passwd001")
        driver.find_element_by_id('TANGRAM__PSP_3__verifyCodeSend').click()
        driver.find_element_by_id('TANGRAM__PSP_3__isAgree').click()
        time.sleep(2)
time.sleep(10)
driver.quit()
