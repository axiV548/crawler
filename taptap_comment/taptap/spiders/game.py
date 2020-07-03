# -*- coding: utf-8 -*-
import scrapy
from taptap.items import GameItem

class TapSpider(scrapy.Spider):
    name = 'game'
    allowed_domains = ['taptap.com']
    url = 'https://www.taptap.com/app/'
    custom_settings = {'ITEM_PIPELINES':{'taptap.pipelines.TapgamePipeline': 300}}
    # 游戏编号 = 168332
    # 评分 = 1
    # 一次 = 1
    # start_urls = [url + str(游戏编号) + '/review?score=' + str(评分) + '&order=update&page=1#review-list']
    # print(start_urls)
    def start_requests(self):
        for x in range(1, 100000):
            user_url = 'https://www.taptap.com/app/' + str(x)
            yield scrapy.Request(user_url, callback=self.parse)

    def parse(self, response):
        # print(response.xpath("//ul"))
        node_list1 = response.xpath("//body")
        for node in node_list1:
            item = GameItem()
            简介集 = []
            类型标签集=[]
            更新内容 = []
            简介 = node.xpath('.//*[@id="description"]/text()').extract()
            # print(node.xpath("./*"))
            游戏名称 = node.xpath('.//div[@class="header-icon-body"]/img/@alt').extract()
            游戏ID = node.xpath('./div[1]/@data-app-id').extract()
            图片 = node.xpath('.//div[@class="header-icon-body"]/img/@src').extract()
            厂商 = node.xpath('.//div[@class="base-info-wrap"]/div/a/span/text()').extract()
            if len(node.xpath('.//div[@class="app-data-wrap"]/p/span/text()[1]').extract()):
                安装数 = node.xpath('.//div[@class="app-data-wrap"]/p/span/text()[1]').extract()
            else:
                安装数 = [0, 0]
            # 简介 = node.xpath('.//*[@id="description"]').extract()
            最近更新内容 = node.xpath('.//*[@id="app-log"]').xpath("string(.)").extract()
            评论数 = node.xpath('./div[1]/div/div/section[1]/div[1]/div[3]/ul/li[2]/a/small/text()').extract()
            社区数 = node.xpath('./div[1]/div/div/section[1]/div[1]/div[3]/ul/li[3]/a/small/text()').extract()
            类型标签 = node.xpath('.//*[@id="appTag"]/li/a/text()').extract()
            if len(node.xpath('./div[1]/div/div/section[1]/div[1]/div[1]/div[2]/span/text()').extract()):
                是否推荐 = node.xpath('./div[1]/div/div/section[1]/div[1]/div[1]/div[2]/span/text()').extract()
            else:
                是否推荐 = "0"
            总评分 = node.xpath('.//div[@class="main-header-text"]/div/span/span/span/text()').extract()
            for 类型 in 类型标签:
                类型标签 = [类型.strip('\n ')]
                类型标签集.append(类型标签[0])
            for 简介1 in 简介:
                简介 = [简介1.strip('\n ')]
                简介集.append(简介[0])
            for 更新1 in 最近更新内容:
                最近更新内容 = [更新1.strip('\n ')]
                更新内容.append(最近更新内容[0])
            item['游戏ID'] = 游戏ID
            item['简介'] = 简介集
            item['最近更新内容'] = 更新内容
            item['评论数'] = 评论数
            item['社区数'] = 社区数
            item['类型标签'] = 类型标签集
            item['是否推荐'] = 是否推荐
            item['游戏名称'] = 游戏名称
            item['图片'] = 图片
            item['厂商'] = 厂商
            item['安装数'] = 安装数
            item['总评分'] = 总评分
            yield item
