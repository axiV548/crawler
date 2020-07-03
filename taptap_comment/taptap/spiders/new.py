# -*- coding: utf-8 -*-
import scrapy
from taptap.items import TaptapItem

class TapSpider(scrapy.Spider):
    name = 'new'
    allowed_domains = ['taptap.com']
    url = 'https://www.taptap.com/app/'
    游戏编号 = 84375
    评分 = 1
    start_urls = [url + str(游戏编号) + '/review?score=' + str(评分) + '&order=update&page=1#review-list']

    # print(start_urls)

    def parse(self, response):

        node_list = response.xpath('//*[@id="reviewsList"]/li[@class="taptap-review-item collapse in"]')
        for node in node_list:
            item = TaptapItem()
            # X = node.xpath('./div/div[4]/@class').extract()
            item['用户名'] = node.xpath("./div/div/span/a/text()").extract()
            item['用户ID'] = node.xpath("./div/div/span/@data-user-id").extract()
            item['评论'] = node.xpath("./div/div[@class='item-text-body']").xpath("string(.)").extract()
            item['评论时间'] = node.xpath("./div/div/a/span//text()[1]").extract()
            if len(node.xpath('./div/div[4]/span/text()').extract()):
                item['设备'] = node.xpath('./div/div[4]/span/text()').extract()
            else:
                item['设备'] = "无"
            if len(node.xpath('./div/div[2]/span').extract()):
                item['游戏时间'] = node.xpath('./div/div[2]/span/text()').extract()
            else:
                item['游戏时间'] = "无"
            if len(node.xpath("./div/div[4]/ul/li/button[@data-value='funny']/span[2]/text()").extract()):
                item["欢乐数"] = node.xpath("./div/div[4]/ul/li/button[@data-value='funny']/span[2]/text()").extract()
            else:
                item['欢乐数'] = "无"
            if len(node.xpath("./div/div[4]/ul/li/button[@data-value='up']/span/text()").extract()):
                item["点赞数"] = node.xpath("./div/div[4]/ul/li/button[@data-value='up']/span[2]/text()").extract()
            else:
                item['点赞数'] = "无"
            if len(node.xpath("./div/div[4]/ul/li/button[@data-value='down']/span/text()").extract()):
                item["点踩数"] = node.xpath("./div/div[4]/ul/li/button[@data-value='down']/span/text()").extract()
            else:
                item['点踩数'] = "无"
            item["回复数"] = node.xpath("./div/div[4]/ul/li[4]/button/span/text()").extract()
            yield item
