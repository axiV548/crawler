# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os
import pymysql as pq

class TaptapPipeline(object):
    # name = 'Null'
    # def __init__(self):
    #     self.file = open('/software/python-scrapy/pinglun/new.json', 'wb')
    #     self.file.write('['.encode('utf-8'))
    #
    # def process_item(self, item, spider):
    #     self.name = item['游戏ID']
    #     line = json.dumps(dict(item), ensure_ascii=False) + ","
    #     self.file.write(line.encode('utf-8'))
    #     return item
    #
    # def close_spider(self, spider):
    #     self.file.write('{}]'.encode('utf-8'))
    #     self.file.close()
    #     os.rename('/software/python-scrapy/pinglun/new.json', '/software/python-scrapy/pinglun/' + self.name + '.json')

    def __init__(self):
        self.connect = pq.connect(host='', user='',
                                  passwd='', db='', charset='utf8')
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        游戏ID = item.get("游戏ID")
        用户名 = item.get("用户名")
        用户ID = item.get("用户ID")
        评论 = item.get("评论")
        评论时间 = item.get("评论时间")
        评分 = item.get("评分")
        设备 = item.get("设备")
        游戏时间 = item.get("游戏时间")
        欢乐数 = item.get("欢乐数")
        点赞数 = item.get("点赞数")
        if len(点赞数):
            点赞数 = 点赞数[0]
        else:
            点赞数 = '0'
        点踩数 = item.get("点踩数")
        回复数 = item.get("回复数")
        # print("wwwww", 用户ID)
        # print("wwwww", 游戏ID)
        print("点赞数", 点赞数)
        print("回复数", 回复数)
        # print("wwwww", 游戏时间)
        
        UserSql = "insert into gametouser(U_ID, G_ID, U_name, I_TIME, D_START, G_TIME, D_CONTENT, G_EQUTPTMENT, D_HAPPY, D_AGRESS, D_DISAGRESS, REPLY) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        try:
            self.cursor.execute(UserSql, (用户ID[0], 游戏ID, 用户名[0], 评论时间[0], 评分, 游戏时间, 评论[0], 设备[0], 欢乐数[0], 点赞数, 点踩数, 回复数))
            self.connect.commit()
        except:
            print("错误！！！")
        return item

    def close_spider(self, spider):
        # self.file.write('{}]'.encode('utf-8'))
        # self.file.close()
        self.cursor.close()
        self.connect.close()


class TapusrPipeline(object):

    def __init__(self):
        # self.file = open('user.json', 'wb')
        # self.file.write('['.encode('utf-8'))
        self.connect = pq.connect(host='', user='',
                                  passwd='', db='', charset='utf8')
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        # line = json.dumps(dict(item), ensure_ascii=False)+","
        # self.file.write(line.encode('utf-8'))
        # return item
        # try:
        用户ID = item.get("用户ID")
        # print("玩过的游戏ID", 游戏ID)

        if item["玩过的游戏"]:
            games = item["玩过的游戏"]
            # print("games", games)
            for game in games:
                游戏ID = game.get("玩过的游戏ID")
                游戏名称 = game.get("游戏名称")
                游戏时长 = game.get("游戏时长")
                游戏类型 = game.get("游戏类型")
                游戏类型 = ",".join(游戏类型)
                # print(游戏ID, 用户ID, 游戏名称, 游戏时长, 类型标签)
                ReSql = "insert into recentplay(G_ID, U_ID, G_TIME) values(%s, %s, %s);"
                # print("wwwww", 游戏类型)
                self.cursor.execute(ReSql, (游戏ID[0], 用户ID[0], 游戏时长[0]))
                self.connect.commit()
        玩的最久 = item.get("玩的最久")
        用户名 = item.get("用户名")
        粉丝数 = item.get("粉丝数")
        关注数 = item.get("关注数")
        收藏数 = item.get("收藏数")
        玩过的游戏数 = item.get("玩过游戏数")
        # 玩的最久数 = item.get("标题")
        评价数 = item.get("评价数")
        # print(用户ID, 用户名, 粉丝数, 关注数, 收藏数, 玩过的游戏数, 评价数)
        print("玩的最久", 玩的最久)
        
        UserSql = "INSERT INTO tapuser(U_ID, U_NAME, FANS, ATTENTION, COLLECT, PLAY, L_PLAY, APPRAISE) values(%s, %s, %s, %s, %s, %s, %s, %s);"

        URLupdate = 'UPDATE tapuser SET U_NAME = %s,FANS = %s,ATTENTION = %s,COLLECT = %s,PLAY = %s,L_PLAY = %s, APPRAISE = %s WHERE U_ID = %s'
        #
        try:
            self.cursor.execute(UserSql, (用户ID[0], 用户名[0], 粉丝数[0], 关注数[0], 收藏数[0], 玩过的游戏数[0], 玩的最久[0], 评价数[0]))
            self.connect.commit()
        except:
            self.cursor.execute(URLupdate, (用户名[0], 粉丝数[0], 关注数[0], 收藏数[0], 玩过的游戏数[0], 玩的最久[0], 评价数[0], 用户ID[0]))
            self.connect.commit()
        else:
            print("错误！！！")

        return item


    def close_spider(self, spider):
        # self.file.write('{}]'.encode('utf-8'))
        # self.file.close()
        self.cursor.close()
        self.connect.close()

class TapgamePipeline(object):
    # def __init__(self):
    #     self.file = open('game.json', 'wb')
    #     self.file.write('['.encode('utf-8'))
    #
    # def process_item(self, item, spider):
    #     line = json.dumps(dict(item), ensure_ascii=False)+","
    #     self.file.write(line.encode('utf-8'))
    #     return item
    #
    # def close_spider(self, spider):
    #     self.file.write('{}]'.encode('utf-8'))
    #     self.file.close()


    def __init__(self):
        self.connect = pq.connect(host='', user='root',
                                  passwd='', db='', charset='utf8')
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):

        游戏ID = item.get("游戏ID")[0]
        简介 = item.get("简介")[0]
        更新内容 = item.get("更新内容")
        if 更新内容:
            更新内容 = item.get("更新内容")[0]
        else:
            更新内容 = None
        评论数 = item.get("评论数")[0]
        社区数 = item.get("社区数")[0]
        类型标签 = item.get("类型标签")[0]
        是否推荐 = item.get("是否推荐")[0]
        游戏名称 = item.get("游戏名称")[0]
        图片 = item.get("图片")[0]
        厂商 = item.get("厂商")[1]
        关注数 = item.get("安装数")[1]
        关注数1 = []
        安装数1 = []
        if 关注数:
            for 关注 in 关注数:
                关注数 = [关注.strip(' 人关注')]
                关注数1.append(关注数[0])
            关注数1 = [x for x in 关注数1 if x != '']
            关注数1 = "".join(关注数1)
            关注数 = 关注数1
            print("关注数", 关注数1)
        安装数 = item.get("安装数")[0]

        if 安装数:
            for 安装 in 安装数:
                安装数 = [安装.strip(' 人安装')]
                安装数1.append(安装数[0])
            安装数1 = [x for x in 安装数1 if x != '']
            安装数1 = "".join(安装数1)
            安装数 = 安装数1
            print("安装数", 安装数1)
        总评分 = item.get("总评分")

        # print("wdnmd",关注数, 安装数)

        GameSql = "insert into game(G_ID, G_NAME, BREIF, R_CONTENT, R_NUMBER, C_NUMBER, VENDER, A_DRADE, T_TAGLTB, RECOMMENT, DOWNLOAD, ATTENTION, URL) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        self.cursor.execute(GameSql, (游戏ID, 游戏名称, 简介, 更新内容, 评论数, 社区数, 厂商, 总评分, 类型标签, 是否推荐, 关注数, 安装数, 图片))
        self.connect.commit()
        # except:
        #     print("错误！！！")
        return item


    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()
