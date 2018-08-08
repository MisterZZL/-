"""
    需求：
        获取悟空问答平台特定关键字搜索答案保存为excel文件
        如搜python会跳转到：https://www.wukong.com/search/?keyword=python
        保存为：悟空问答_python.xlsx
"""
import os
import requests
import time
import xlsxwriter  # excel读写 xlsxwriter
from collections import OrderedDict

TITLE_NAMES = ["问题pid", "问题", "提问时间", "提问者名称", "提问者uid", "提问者头像链接",
               "问题被收藏数", "好的回答数", "普通回答数", "解答者", "解答者id", "答案id", "答案"]
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}


def timestamp_2_str(time_stamp):
    """unix时间戳转时间字符串"""
    struct_time = time.localtime(time_stamp)
    str_time = time.strftime('%Y-%m-%d %H:%M:%S', struct_time)
    return str_time


# 解析数据
def parse_data(rsp_json):
    """ 解析数据"""
    has_more = False
    data_list = list()

    if not isinstance(rsp_json, dict):
        print("待解析数据格式非法:%s" % (rsp_json))
        return has_more, data_list

    if rsp_json.get("err_no", None) != 0:
        print("获取数据非法，:%s" % (rsp_json.get("err_tips")))
        return has_more, data_list

    data = rsp_json.get("data", None)
    if data:
        has_more = data.get("has_more", "false")
        feed_questions = data.get("feed_question", [])
        for i in feed_questions:
            q_info = OrderedDict()
            ans_list = i.get("ans_list", [])
            question = i.get("question", None)
            if not question:
                break
            q_info["qid"] = question["qid"]
            q_info["title"] = question["title"]
            q_info["create_time_human"] = timestamp_2_str(int(question["create_time"]))
            q_info["uname"] = question["user"]["uname"]
            q_info["user_id"] = question["user"]["user_id"]
            q_info["avatar_url"] = question["user"]["avatar_url"]
            q_info["follow_count"] = question["follow_count"]
            q_info["nice_ans_count"] = question["nice_ans_count"]
            q_info["normal_ans_count"] = question["normal_ans_count"]
            if ans_list:
                ans1 = ans_list[0]
                q_info["ans_user"] = ans1["user"]["uname"]
                q_info["ans_user_id"] = ans1["user"]["user_id"]
                q_info["ansid"] = ans1["ansid"]
                q_info["abstract_text"] = ans1["abstract_text"]
            data_list.append(q_info)
    return has_more, data_list


# 数据写入excel
def write_data_to_excel(work_book, data_list, row_num):
    worksheet_name = '悟空爬虫数据'
    work_sheet = work_book.get_worksheet_by_name(worksheet_name)
    if not work_sheet:
        # 如果不存在则创建工作表
        work_sheet = work_book.add_worksheet(worksheet_name)
        row_num = 0
        work_sheet.write_row(row_num, 0, TITLE_NAMES)
        row_num += 1
    for i in data_list:
        work_sheet.write_row(row_num, 0, i.values())
        row_num += 1
    return row_num


# 根据输入关键字 爬取内容并存储
def save_search_url_data(work_book, search_url, row_num):
    rsp_json = requests.get(search_url, headers=HEADERS).json()
    # 解析数据 接口调用返回的 dict ---->>> [[q1],[q2]...]
    has_more, data_list = parse_data(rsp_json)
    # 将数据写入excel
    row_num = write_data_to_excel(work_book, data_list, row_num)
    return has_more, row_num


def main(keyword):
    os.makedirs('output', exist_ok=True)
    filename = os.path.join('output', '悟空问答_%s.xlsx' % keyword)
    base_url = 'https://www.wukong.com/wenda/web/search/loadmore/?search_text=%s&offset=%s&count=%s'
    excel_work_book = xlsxwriter.Workbook(filename)  # 可以改造成上下文
    count = 20  # 每页所爬条数
    offset = 0  # 当前偏移数，如按 10页每条来爬， 去爬第一页时是 10， 爬第二页是是 20
    row_num = 0  # excel写至行数
    has_more = True  # 存储服务端响应的是否还有下一页
    while has_more:
        search_url = base_url % (keyword, offset, count)
        # 得到是否还有下一页以及excel写到哪里了
        has_more, row_num = save_search_url_data(excel_work_book, search_url, row_num)
        # 由于包含了头部需减一处理
        print("已爬取%s条....." % (row_num - 1))
        offset += count
    excel_work_book.close()


if __name__ == "__main__":
    keyword = input('请输入关键字:')
    main(keyword)
