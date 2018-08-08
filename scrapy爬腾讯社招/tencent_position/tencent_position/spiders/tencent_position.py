import scrapy

from tencent_position.items import TencentPositionItem


class TencentPositionSpider(scrapy.Spider):
    name = 'tencent_position'
    allowed_domains = ['tencent.com']
    urls = 'https://hr.tencent.com/position.php?&start='

    offset = 0
    # 起始url
    start_urls = [urls + str(offset)]
    max_num = 0

    def parse(self, response):
        pages = response.xpath('//*[@class="pagenav"]/a/text()').extract()
        self.max_num = (int(pages[-2]) - 1 * 10)
        yield scrapy.Request(self.urls + str(self.offset), callback=self.page_parse)

    def page_parse(self, response):
        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            # 初始化模型对象
            try:
                item = TencentPositionItem()
                # 职位名称
                item['positionname'] = each.xpath("./td[1]/a/text()").extract()[0]
                # 详情连接
                item['positionlink'] = each.xpath("./td[1]/a/@href").extract()[0]
                # 职位类别
                item['positionType'] = each.xpath("./td[2]/text()").extract()[0]
                # 招聘人数
                item['peopleNum'] = each.xpath("./td[3]/text()").extract()[0]
                # 工作地点
                item['workLocation'] = each.xpath("./td[4]/text()").extract()[0]
                # 发布时间
                item['publishTime'] = each.xpath("./td[5]/text()").extract()[0]
                yield item
            except:
                print("报错%s" % (response.url))
        if self.offset < self.max_num:
            self.offset += 10
            # 每次处理完一页的数据之后，重新发送下一页页面请求
            # self.offset自增10，同时拼接为新的url，并调用回调函数self.parse处理Response
            yield scrapy.Request(self.urls + str(self.offset), callback=self.page_parse)