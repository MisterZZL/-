'''
    1.  爬取以下站点中各个明星图片，分别单独建文件夹存放。
        起始URL地址：http://www.mm131.com/mingxing
        提交作业代码 上传gitee
'''
import os
import logging
import requests
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO)


def store_girl_img(girl_url, store_girl_dir):
    # 把girl_url的单个小姐姐放入store_girl_dir文件夹
    girl_html = requests.get(girl_url)          #访问girl_url网址
    girl_html.encoding = "gbk"                  #修改编码，不然会是乱码
    girl_text = girl_html.text                  #获取girl_html的网页内容。girl_html.content返回的是bytes数据

    girl_src = BeautifulSoup(girl_text, 'lxml').find("div",class_='content-pic').find('img')['src']
    #BeautifulSoup用lxml库解析girl_html的网页内容，并找到所有class_='content-pic'的div标签
    #再找到img标签下的src属性，得到单张照片的链接
    print(girl_src)

    # 此处加headers是为防反爬虫，如果不加会响应403，没有权限
    headers = {
        'Referer': girl_url,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    file_name = girl_src.split('/')[-1]
    #将http://img1.mm131.me/pic/2016/1.jpg切片成["http://img1.mm131.me/pic/2016"，"1.jpg"],[-1]就是去第二个1.jpg
    file_name = os.path.join(store_girl_dir, file_name) #在store_girl_dir目录下创建图片名字file_name，如1.jpg
    with open(file_name, 'wb') as f:            #二进制模式打开file_name
        girl_content = requests.get(girl_src, headers=headers).content   # .content获取图片的二进制数据
        f.write(girl_content)                   #写入到file_name


def store_page_grils(href, store_girl_dir):
    # 把href这个链接下的小姐姐们（多个）放入文件夹store_girl_dir
    girl_text = requests.get(href).text         #访问某个美女的图片页面
    soup = BeautifulSoup(girl_text, 'lxml')     #获得BeautifulSoup对象
    # 获取美女图片的张数
    max_page_num = soup.find('div', class_='content-page').find_all('a')[-2].get_text()
    #找到class_='content-page'的div标签---->找出该div下所有的a标签，得到一个a标签列表
    #[-2]取出倒数第二个按标签，get_text()是获取文本内容
    max_page_num = int(max_page_num)   #文本内容转化为整数

    girl_url_list = [href] #定义一个列表，存放一个美女所有图片的链接，页面特殊，href表示第一张
    #for循环获取第二张到最后一张的链接
    for page_num in range(2, max_page_num + 1):

        girl_url = str(href).replace(".html",f"_{page_num}.html") # 将.html替换_{page_num}.html
        # print(girl_url)
        girl_url_list.append(girl_url)      #将第二张到最后一张的链接追加到girl_url_list
    # print(girl_url_list)
    for girl_url in girl_url_list:
        store_girl_img(girl_url, store_girl_dir)  #循环调用store_girl_img函数


def main():
    url = 'http://www.mm131.com/mingxing'
    store_dir = 'meizitu'                   #主目录
    os.makedirs(store_dir, exist_ok=True)   #创建主目录，若主目录存在不报错
    home_html = requests.get(url)           #访问http://www.mm131.com/mingxing
    home_html.encoding = "gbk"
    home_text = home_html.text              #获取网页内容
    # 得到小姐姐们的链接标签
    ahref_list = BeautifulSoup(home_text, 'lxml').find("div",class_="main").find_all('a')[2:22]
    #找到所有a标签，得到一个a标签列表，[2:22]表示：取a标签列表的第2到21个，因为前两个是不需要的
    # print(ahref_list)
    for ahref in ahref_list:            #遍历这20个a标签
        # ahref 是bs4.element.Tag实例
        girlname = ahref.get_text()  # 获取a标签的文本内容，作为存放小姐姐图片的子目录
        href = ahref['href']# 取出a标签的href属性，得到一个小姐姐图片的链接
        store_girl_dir = os.path.join(store_dir, girlname)  # 拼接得到放该小姐的房间号，即存放美女的文件夹
        os.makedirs(store_girl_dir, exist_ok=True)
        logging.info(f'开始下载{girlname}的图片')
        store_page_grils(href, store_girl_dir)


if __name__ == '__main__':
    main()
