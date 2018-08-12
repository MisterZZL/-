#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import os,datetime
import xlsxwriter
import openpyxl
from openpyxl import styles,Workbook


output_dir = os.makedirs('output', exist_ok=True)
source_dir = 'source'  #邮件存放目录

# 1 建立 工作簿 及工作表
gzb_name = "output/邮件汇总.xlsx"
workbook = xlsxwriter.Workbook(gzb_name)
# 工作表名称
sheet_name = "sheet1"
worksheet = workbook.add_worksheet(sheet_name)

worksheet.set_column('A:A', 60)         #设置列宽
worksheet.set_column('B:B', 100)        #设置列宽

# 填充表格数据
# 表头  第一行数据
title_name = ["主题", "内容", ]

format_title = workbook.add_format()            #设置背景颜色（不知道为什么要写两行才能成功加上）
format_title.set_bg_color("red")

worksheet.write_row("A1", title_name,cell_format=format_title)       #注意write和write_row的区别


#
# worksheet.write_row("A1", title_name, format_title)
for index,email in enumerate((os.listdir('source')),start=2):
    email_file = os.path.join('source',email)
    with open(email_file,'r',encoding='utf-8') as f:
        title = f.readline()
        content = f.read()
        worksheet.write(f"A{index}",title)
        worksheet.write(f"B{index}",content)

