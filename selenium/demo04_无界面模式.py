from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options

chrome_o = Options()
chrome_o.add_argument('--headless')  # 不打开浏览器
chrome_o.add_argument('--disable-gpu')  # 禁用gpu运算

wd = webdriver.Chrome(chrome_options=chrome_o)
wd.get('https://www.baidu.com')

print(wd.title)  # 没打开浏览器也得到了百度的标题
wd.quit()
