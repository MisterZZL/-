#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import time,os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


os.makedirs('output', exist_ok=True)

'''
1 第一步打开qq邮箱的页面
2 切换到账号或密码登录
3 输入账号和密码
4 点击登录按钮
'''

# chrome_o = Options()
# chrome_o.add_argument('--headless')  # 不打开浏览器
# chrome_o.add_argument('--disable-gpu')  # 禁用gpu运算
# wd = webdriver.Chrome(chrome_options=chrome_o)
wd = webdriver.Chrome() #设置对应浏览器的驱动
wd.implicitly_wait(10)  #implicitly_wait()默认参数的单位为秒，全局有效

wd.get('https://mail.qq.com/')
login_frame = wd.find_element_by_id('login_frame')
wd.switch_to.frame(login_frame)  # 切换到框架内
switcher_plogin = wd.find_element_by_id('switcher_plogin')
switcher_plogin.click()

QQ = "QQ账号"
PASSWORD = "****QQ密码*****"
wd.find_element_by_id('u').send_keys(QQ)
wd.find_element_by_id('p').send_keys(PASSWORD)
wd.find_element_by_id('login_button').click()

'''
1、点击收件箱
2、切换到收信列表iframe
3、获取邮箱页数
'''
# wd.find_element(By.ID,"readmailbtn_link").click()
# # main_frame = wd.find_element_by_id("mainFrame")
# # wd.switch_to.frame(main_frame)
wd.find_element_by_xpath('//*[@id="folder_1_td"]').click()
main_frame = wd.find_element_by_id("mainFrame")
# main_frame = wd.find_elements_by_xpath('//*[@id="mainFrame"]')[0]  #效果同上，因为返回的是列表，
# 在执行wd.switch_to.frame(main_frame)时，需要加上[0]，取出列表的第一个元素

wd.switch_to.frame(main_frame)   #切换到嵌套的页面下

page_num = wd.find_element_by_xpath('//*[@id="frm"]/div[1]/div[1]').text
page_num = page_num[2]
page_num = int(page_num)
print(page_num)

'''
1、获取邮件列表的内容
2、遍历邮件列表的记录，然后右键选择在新窗口中打开
3、切换到新的句柄
4、获取邮件内容
5、关闭新打开的窗口，回到第一个句柄
6、继续2
'''
for page in range(1,page_num+1):
    print(f"第{page}页")
    h = wd.current_window_handle  # 获取当前句柄
    first_page_email_eles = wd.find_elements_by_css_selector('.toarea .F, .toarea .M')  # 获取邮件列表
    # 注意区别 wd.find_elements_by_css_selector('.toarea .F, .toarea .M')--->一组。返回列表
    #         wd.find_element_by_css_selector('.toarea .F, .toarea .M') --->一个
    first_page_email_eles_count = len(first_page_email_eles)  # 获取邮件列表的长度

    for i in range(first_page_email_eles_count):
        email_ele = first_page_email_eles[i]
        # 右键操作
        ActionChains(wd).context_click(email_ele).perform()
        # 选择在新窗口中打开
        # 右键下拉菜单[ ]的第2个元素，索引为[1]
        wd.find_elements_by_class_name('menu_item')[1].click()

        wd.switch_to.window(wd.window_handles[1])  # 切换到新打开的窗口

        # 邮件内容是嵌套的另一个页面的，所以获取邮件内容所在的页面
        # 也就是找到其iframe，并切换
        main_frame = wd.find_element_by_id('mainFrame')
        wd.switch_to.frame(main_frame)

        # 获取邮件的信息
        email_subject = wd.find_element_by_id('subject').text
        email_content = wd.find_element_by_id('mailContentContainer').text  # .text获取文本内容
        print(email_subject)

        with open(f"./output/第{page}页邮件{i}.txt","w",encoding="utf-8")as file:
            # pass
            file.write(str(email_subject))
            file.write("\n")
            file.write(str(email_content))
        time.sleep(0)

        wd.close()  # 关闭当前句柄
        wd.switch_to.window(h)  # 关闭窗口

        main_frame = wd.find_element_by_id('mainFrame')  # 找到收件箱的iframe
        wd.switch_to.frame(main_frame)  # 切换到收件箱的iframe

    if page < page_num:
        wd.find_element_by_id('nextpage').click()

    # else:break

wd.quit()# 关闭浏览器
