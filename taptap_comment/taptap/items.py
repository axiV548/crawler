# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class GameItem(scrapy.Item):
    游戏ID= scrapy.Field()
    简介= scrapy.Field()
    评论数= scrapy.Field()
    社区数= scrapy.Field()
    类型标签集= scrapy.Field()
    是否推荐= scrapy.Field()
    游戏名称= scrapy.Field()
    图片= scrapy.Field()
    厂商= scrapy.Field()
    安装数= scrapy.Field()
    总评分= scrapy.Field()
    最近更新内容= scrapy.Field()
    类型标签= scrapy.Field()

class TaptapItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    用户名 = scrapy.Field()
    游戏名称 = scrapy.Field()
    图片 = scrapy.Field()
    厂商 = scrapy.Field()
    安装数 = scrapy.Field()
    总评分 = scrapy.Field()
    用户ID = scrapy.Field()
    评论       = scrapy.Field()
    评论时间     = scrapy.Field()
    评分      = scrapy.Field()
    游戏ID= scrapy.Field()
    设备= scrapy.Field()
    游戏时间= scrapy.Field()
    欢乐数= scrapy.Field()
    点赞数= scrapy.Field()
    点踩数= scrapy.Field()
    回复数= scrapy.Field()
    简介= scrapy.Field()
    最近更新内容= scrapy.Field()
    评论数= scrapy.Field()
    社区数= scrapy.Field()
    类型标签= scrapy.Field()
    是否推荐= scrapy.Field()

class UserItem(scrapy.Item):
    用户名 = scrapy.Field()
    用户ID =scrapy.Field()
    签名 = scrapy.Field()
    收到的赞 =scrapy.Field()
    收到的欢乐=scrapy.Field()
    粉丝数 =scrapy.Field()
    关注数 =scrapy.Field()
    收藏数 =scrapy.Field()
    玩过游戏数=scrapy.Field()
    玩的最久 = scrapy.Field()
    评价数 = scrapy.Field()
    帖子数 = scrapy.Field()
    回复数 = scrapy.Field()
    玩过的游戏 = scrapy.Field()
    游戏集 = scrapy.Field()
