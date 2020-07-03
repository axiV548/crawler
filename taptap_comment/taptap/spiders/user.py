# -*- coding: utf-8 -*-
import scrapy
from taptap.items import UserItem
import pymysql as pq

class TapSpider(scrapy.Spider):
    name = 'user'
    allowed_domains = ['taptap.com']
    url = 'https://www.taptap.com/user/'
    # 用户ID = 13674013
    # start_urls = [url + str(游戏编号) + '/review?score=' + str(评分) + '&order=update&page=' + str(页码) + '#review-list']
    # start_urls = ['https://www.taptap.com/user/'+str(用户ID)]
    custom_settings = {'ITEM_PIPELINES': {'taptap.pipelines.TapusrPipeline': 300}}
    # print(start_urls)

    def start_requests(self):
        cookies = ""
        cookies = {i.split("=")[0]:i.split("=")[1] for i in cookies.split("; ")}
        # file = [13674013]

        connect = pq.connect(host='', user='',
                             passwd='', db='', charset='utf8')
        cursor = connect.cursor()
        sql_countAll = 'select a.`U_ID` as U_ID FROM gametouser AS a WHERE a.`U_ID` NOT IN (SELECT b.`U_ID` FROM tapuser b) GROUP BY a.`U_ID`'
        cursor.execute(sql_countAll)
        countAll = cursor.fetchall()
        cursor.close()
        connect.close()
        for idd in countAll:
            user_url = 'https://www.taptap.com/user/' + str(idd[0])
            # print('no3', user_url)
            # yield scrapy.Request(user_url, callback=self.parse)
            yield scrapy.Request(user_url, callback=self.parse, cookies=cookies)

        # user_url = 'https://www.taptap.com/user/' + str(x)
        # yield scrapy.Request(user_url, callback=self.parse, cookies=cookies)

        # with open('C:/py3/test/' + str(self.游戏编号) + '.json', 'r', encoding='utf-8') as js:
        #     file = json.load(js)
        #     for y in file:
        #         try:
        #             x = y['用户ID'][0]
        #             user_url = 'https://www.taptap.com/user/' + str(x)
        #             yield scrapy.Request(user_url, callback=self.parse, cookies=cookies)
        #
        #         except:
        #             print('null')
        #     js.close()
        #
        # for x in file:
        #     user_url = 'https://www.taptap.com/user/' + str(x)
        #     print('no3', user_url)
        #     # yield scrapy.Request(user_url, callback=self.parse)
        #     yield scrapy.Request(user_url, callback=self.parse, cookies=cookies)

    def parse(self, response):
        user2 = response.xpath('//body')
        # print('url',response.url)
        game_url = str(response.url)+'?page=1'
        user3 = response.xpath('//*[@id="played"]/section/ul/li')
        user_list = []
        # print(user_list1)
        for user in user2:
            item = UserItem()
            用户id集= []
            用户id = user.xpath(".//div[@class='user-all-info']/span[1]/text()").extract()
            for i in 用户id:
                用户 = [i.strip("ID:")]
                用户id集.append(用户[0])
            用户名 = user.xpath(".//div[@class='user-all-info']/h1/text()").extract()
            if len(user.xpath("./div[1]/div[1]/div/section/div[1]/div/p[1]/text()").extract()):
                签名 = user.xpath("./div[1]/div[1]/div/section/div[1]/div/p[1]/text()").extract()
            else:
                签名='Null'
            if len(user.xpath(".//p[@class='left-text-vote']/span[1]/text()").extract()):
                收到的赞 = user.xpath(".//p[@class='left-text-vote']/span[1]/text()").extract()
            else:
                收到的赞 = "0"
            if len(user.xpath(".//p[@class='left-text-vote']/span[2]/text()").extract()):
                收到的欢乐 = user.xpath(".//p[@class='left-text-vote']/span[2]/text()").extract()
            else:
                收到的欢乐 = "0"
            if len(user.xpath("./div[1]/div[1]/div/section/div[2]/ul/li[1]/a/span[1]/text()").extract()):
                粉丝数 = user.xpath("./div[1]/div[1]/div/section/div[2]/ul/li[1]/a/span[1]/text()").extract()
            else:
                粉丝数 = "0"
            if len(user.xpath("./div[1]/div[1]/div/section/div[2]/ul/li[2]/a/span[1]/text()").extract()):
                关注数 = user.xpath("./div[1]/div[1]/div/section/div[2]/ul/li[2]/a/span[1]/text()").extract()
            else:
                关注数 = "0"
            if len(user.xpath("./div[1]/div[1]/div/section/div[2]/ul/li[3]/a/span[1]/text()").extract()):
                收藏数 = user.xpath("./div[1]/div[1]/div/section/div[2]/ul/li[3]/a/span[1]/text()").extract()
            else:
                收藏数 = "0"
            if len(user.xpath(".//*[@id='played-tab']/span/text()").extract()):
                玩过游戏数 = user.xpath(".//*[@id='played-tab']/span/text()").extract()
            else:
                玩过游戏数 = "0"
            if len(user.xpath(".//*[@id='reviews-tab']/span/text()").extract()):
                评价数 = user.xpath(".//*[@id='reviews-tab']/span/text()").extract()
            else:
                评价数 = "0"
            if len(user.xpath(".//*[@id='topics-tab']/span/text()").extract()):
                帖子数 = user.xpath(".//*[@id='topics-tab']/span/text()").extract()
            else:
                帖子数 = "0"
            if len(user.xpath(".//*[@id='posts-tab']/span/text()").extract()):
                回复数 = user.xpath(".//*[@id='posts-tab']/span/text()").extract()
            else:
                回复数 = "0"
            if len(user.xpath(".//*[@id='most-played-tab']/span/text()").extract()):
                玩的最久 = user.xpath(".//*[@id='most-played-tab']/span/text()").extract()
            else:
                玩的最久 = "0"

            item['用户名'] =用户名
            item['用户ID'] =用户id集
            item['签名'] =签名
            item['收到的赞'] =收到的赞
            item['收到的欢乐'] =收到的欢乐
            item['粉丝数'] =粉丝数
            item['关注数'] =关注数
            item['收藏数'] =收藏数
            item['玩过游戏数'] =玩过游戏数
            item['评价数'] =评价数
            item['帖子数'] =帖子数
            item['回复数'] =回复数
            item['玩的最久'] = 玩的最久
            # yield item

        if user3:
            yield scrapy.Request(game_url, callback=self.parse_next, meta={"item": item, "user_list": user_list})

    def parse_next(self, response):

        reviews_page = response.xpath('//*[@id="reviews-tab"]').extract()
        item = response.meta["item"]
        user_list = response.meta["user_list"]
        user3 = response.xpath('//*[@id="played"]/section/ul/li')
        next_play_game = response.xpath("//*[@id='played']/section/div[2]/section/ul/li[last()]/a/@href").extract()
        for user1 in user3:
            user_D={}
            玩过的游戏集 = []
            玩过的游戏I = []
            玩过的游戏ID = user1.xpath("./@id").extract()
            玩过的游戏 = user1.xpath("./div/h2//text()").extract()
            玩过的游戏评分 = user1.xpath("./div/span[1]/text()").extract()
            玩过的游戏类型 = user1.xpath("./div/p/span/text()").extract()
            if len(user1.xpath("./div/span[2]/text()").extract()):
                玩过的游戏时长 = user1.xpath("./div/span[2]/text()").extract()
            else:
                玩过的游戏时长 = "0"
            # 玩过的游戏时长 = user1.xpath("./section/ul/li/div/span[2]/text()").extract()
            for i in 玩过的游戏:
                玩过的游戏 = [i.strip("\n ")]
                玩过的游戏集.append(玩过的游戏[0])
            for p in 玩过的游戏ID:
                玩过的游戏ID = [p.strip("played-")]
                玩过的游戏I.append(玩过的游戏ID[0])

            玩过的游戏集 = [x for x in 玩过的游戏集 if x != '']
            # print("玩过的游戏" + str(玩过的游戏集))
            # print("玩过的游戏评分" + str(玩过的游戏评分))
            # print("玩过的游戏时长" + str(玩过的游戏时长))
            # print("玩过的游戏类型" + str(玩过的游戏类型))
            # item['玩过的游戏'] =玩过的游戏集
            # item['玩过的游戏评分'] =玩过的游戏评分
            # item['玩过的游戏类型'] =玩过的游戏类型
            # item['玩过的游戏时长'] =玩过的游戏时长
            user_D['游戏名称'] =玩过的游戏集
            user_D['游戏评分'] =玩过的游戏评分
            user_D['游戏类型'] =玩过的游戏类型
            user_D['游戏时长'] =玩过的游戏时长
            user_D['玩过的游戏ID'] = 玩过的游戏I
            user_list.append(user_D)
            # print(user_list)

            # yield item
        # print('user_list',user_list)
        if next_play_game:
            next_page = next_play_game[0]
            yield scrapy.Request(next_page, callback=self.parse_next, meta={"item": item, "user_list": user_list})
        else:
            item['玩过的游戏'] = user_list
            yield item
            # print('user_list', user_list)
        # elif reviews_page:
        #     reviews_url = self.url + str(self.用户ID)+"/reviews"
        #     yield scrapy.Request(reviews_url, callback=self.pare_reviews)


    #
