'''
    需求：获取网址 http://www.mzitu.com/all/  下最新月份的的所有妹子图片，并分文件夹放入 meizitu 文件夹中
    最终目录结构如: meizitu/18岁MM久久Aimee：可以甜美也可以狂野的御姐养成记/29c01.jpg
'''
import os
import logging

import re
import requests
from bs4 import BeautifulSoup
from multiprocessing import Process, Pool

logging.basicConfig(level=logging.INFO)


def store_girl_img(girl_url, store_girl_dir):
    # 把girl_url的单个小姐姐放入store_girl_dir文件夹
    girl_text = requests.get(girl_url).text
    girl_src = BeautifulSoup(girl_text, 'lxml').find(class_='main-image').find('img')['src']
    # 此处加headers是为防反爬虫，如果不加会响应403，没有权限
    headers = {
        'Referer': girl_url,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    file_name = girl_src.split('/')[-1]
    file_name = os.path.join(store_girl_dir, file_name)
    with open(file_name, 'wb') as f:
        girl_content = requests.get(girl_src, headers=headers).content
        f.write(girl_content)


def store_page_grils(href, store_girl_dir):
    # 把href这个链接下的小姐姐们（多个）放入文件夹store_girl_dir
    logging.info(f'开始下载{href} 下的图片')
    girl_text = requests.get(href).text
    soup = BeautifulSoup(girl_text, 'lxml')
    # 得到小姐姐的数量
    max_page_num = soup.find('div', class_='pagenavi').find_all('span')[-2].get_text()
    max_page_num = int(max_page_num)

    for page_num in range(1, max_page_num + 1):
        girl_url = f'{href}/{str(page_num)}'
        store_girl_img(girl_url, store_girl_dir)
    logging.info(f'已下载完{href} 下的图片')


def main():
    url = 'http://www.mzitu.com/all/'
    store_dir = 'meizitu'
    os.makedirs(store_dir, exist_ok=True)
    home_text = requests.get(url).text
    # 得到小姐姐们的链接标签
    pool = Pool()
    ahref_list = BeautifulSoup(home_text, 'lxml').find('ul', class_='archives').find_all('a')
    for ahref in ahref_list:
        # ahref 是bs4.element.Tag实例
        girlname = ahref.get_text().replace(' ', '').replace(':', '').replace('?', '')  # 获取a标签的文本内容：如 18岁MM久久Aimee：可以甜美也可以狂野的御姐养成记
        href = ahref["href"]  # 取出a标签的href属性
        BASE_DIR = os.path.dirname(__file__)
        store_girl_dir = os.path.join(BASE_DIR, store_dir, girlname)  # 拼接得到放该小姐的房间号，即存放美女的文件夹
        os.makedirs(store_girl_dir, exist_ok=True)
        pool.apply_async(store_page_grils, args=(href, store_girl_dir))

    pool.close()
    pool.join()
    logging.info('图片下载完成')


if __name__ == '__main__':
    main()
