from selenium import webdriver
from selenium.webdriver import ActionChains

'''
1 第一步打开qq邮箱的页面
2 切换到账号或密码登录
3 输入账号和密码
4 点击登录按钮
'''

wd = webdriver.Chrome()
wd.implicitly_wait(10)

wd.get('https://mail.qq.com/')

# 找不到是因为元素嵌套在了iframe里面，需要先将wd切换到iframe

login_frame = wd.find_element_by_id('login_frame')
wd.switch_to.frame(login_frame)  # 切换到框架内
switcher_plogin = wd.find_element_by_id('switcher_plogin')
switcher_plogin.click()

# from settings import QQ, PASSWORD
# 大家需要把这里改成自己的qq和密码
QQ = '123'  # qq号
PASSWORD = '123'  # qq密码

wd.find_element_by_id('u').send_keys(QQ)
wd.find_element_by_id('p').send_keys(PASSWORD)

wd.find_element_by_id('login_button').click()

'''
1、点击收信
2、切换到收信列表iframe
'''

wd.find_element_by_id('readmailbtn_link').click()
main_frame = wd.find_element_by_id('mainFrame')
wd.switch_to.frame(main_frame)

'''
1、获取邮件列表的内容
2、遍历邮件列表的记录，然后右键选择在新窗口中打开
3、切换到新的句柄
4、获取邮件内容
5、关闭新打开的窗口，回到第一个句柄
6、继续2
'''
h = wd.current_window_handle  # 获取当前句柄
email_eles = wd.find_elements_by_css_selector('.toarea .F, .toarea .M')  # 获取邮件列表
email_eles_count = len(email_eles)  # 获取邮件列表的长度

for i in range(email_eles_count):
    email_ele = wd.find_elements_by_css_selector('.toarea .F, .toarea .M')[i]
    # 右键操作
    ActionChains(wd).context_click(email_ele).perform()
    # 选择在新窗口中打开
    wd.find_elements_by_class_name('menu_item')[1].click()

    email_hadle = wd.window_handles[1]  # 获取第二个句柄
    wd.switch_to.window(email_hadle)  # 切换到新的句柄
    # for h_new in wd.window_handles:
    #     if h_new != h:
    #         wd.switch_to_window(h_new)

    main_frame = wd.find_element_by_id('mainFrame')
    wd.switch_to.frame(main_frame)

    email_subject = wd.find_element_by_id('subject').text
    email_content = wd.find_element_by_id(
        'mailContentContainer').text  # .text获取文本内容

    print(email_subject, email_content)

    wd.close()  # 关闭当前句柄
    wd.switch_to.window(h)

    main_frame = wd.find_element_by_id('mainFrame')
    wd.switch_to.frame(main_frame)

import time

time.sleep(3)
wd.quit()
# 关闭浏览器
