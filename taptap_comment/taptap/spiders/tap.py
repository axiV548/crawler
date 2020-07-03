# -*- coding: utf-8 -*-
import scrapy
from taptap.items import TaptapItem
import json

class TapSpider(scrapy.Spider):
    name = 'tap'
    allowed_domains = ['taptap.com']
    url = 'https://www.taptap.com/app/'
    评分 = 1
    游戏编号 = 0
    def __init__(self, gameNub=None, *args, **kwargs):
        super(TapSpider, self).__init__(*args, **kwargs)
        print('category', gameNub)
        self.游戏编号 = gameNub
        self.start_urls = [self.url + str(self.游戏编号) + '/review?score=' + str(self.评分) + '&order=update&page=1#review-list']

    custom_settings = {'ITEM_PIPELINES': {'taptap.pipelines.TaptapPipeline': 300}}
    # print(start_urls)

    def parse(self, response):
        游戏编号 = self.游戏编号
        评分 = self.评分
        next_page_args = response.xpath(".//div[@class='main-body-footer']//li[last()]/a/@href").extract()
        # print(response.xpath("//body/text()"))
        node_list = response.xpath('//*[@id="reviewsList"]/li[@class="taptap-review-item collapse in"]')
        for node in node_list:
            游戏ID = str(游戏编号)
            评论集 = []
            temp1 = []
            temp3 = []
            temp5 = []
            temp7 = []
            item = TaptapItem()
            # X = node.xpath('./div/div[4]/@class').extract()
            用户名 = node.xpath("./div/div/span/a/text()").extract()
            用户ID = node.xpath("./div/div/span/@data-user-id").extract()
            评论 = node.xpath("./div/div[@class='item-text-body']").xpath("string(.)").extract()
            评论时间 = node.xpath("./div/div/a/span//text()[1]").extract()
            for i in 评论:
                评论 = [i.strip("\n ")]
                评论集.append(评论[0])
                # 删除列表中的不需要字符
            for x in 评论时间:
                temp = [x.strip("\n ")]
                temp1.append(temp[0])
            for y in temp1:
                temp2 = [y.strip("发布于")]
                temp3.append(temp2[0])
            for z in temp3:
                temp4 = [z.strip("已修改 >")]
                temp5.append(temp4[0])
            for w in temp5:
                temp6 = [w.strip("Up")]
                temp7.append(temp6[0])
            temp7 = [x for x in temp7 if x != '']
            item['游戏ID'] = 游戏ID
            item['用户名'] = 用户名
            item['用户ID'] = 用户ID
            item['评论'] = 评论集
            item['评论时间'] = temp7
            item['评分'] = 评分
            if len(node.xpath('./div/div[4]/span/text()').extract()):
                item['设备'] = node.xpath('./div/div[4]/span/text()').extract()
            else:
                item['设备'] = "无"
            if len(node.xpath('./div/div[2]/span').extract()):
                item['游戏时间'] = node.xpath('./div/div[2]/span/text()').extract()
            else:
                item['游戏时间'] = "0"
            if len(node.xpath("./div/div[4]/ul/li/button[@data-value='funny']/span[2]/text()").extract()):
                item["欢乐数"] = node.xpath("./div/div[4]/ul/li/button[@data-value='funny']/span[2]/text()").extract()
            else:
                item['欢乐数'] = "0"
            if len(node.xpath("./div/div[4]/ul/li/button[@data-value='up']/span/text()").extract()):
                item["点赞数"] = node.xpath("./div/div[4]/ul/li/button[@data-value='up']/span/text()").extract()
            else:
                item['点赞数'] = "0"
            if len(node.xpath("./div/div[4]/ul/li/button[@data-value='down']/span/text()").extract()):
                item["点踩数"] = node.xpath("./div/div[4]/ul/li/button[@data-value='down']/span/text()").extract()
            else:
                item['点踩数'] = "0"
            回复数 = node.xpath("./div/div[4]/ul/li[4]/button/span/text()").extract()
            回复数1 = []
            for 回复 in 回复数:
                回复数 = [回复.strip('回复 ')]
                回复数1.append(回复数[0])
            回复数1 = [x for x in 回复数1 if x != '']
            回复数1 = "".join(回复数1)
            回复数 = 回复数1
            if 回复数:
                item["回复数"] = 回复数
            else:
                item['回复数'] = "0"

            yield item
        if next_page_args:
            next_page = next_page_args[0]
            yield scrapy.Request(next_page, callback=self.parse)
        elif 评分 <= 4:
            self.评分 += 1
            # print("评分" + str(self.评分))
            url_next = self.url + str(游戏编号) + '/review?score=' + str(self.评分) + '&order=update&page=1#review-list'
            # print("评分" + url_next)
            yield scrapy.Request(url_next, callback=self.parse)