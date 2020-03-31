# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FundItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()


class Fund(scrapy.Item):

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.scale = 0  # 亿
        self.birth = ''  # 成立日期
        self.age = 0  # 基金年限
        self.manager = []  # 基金经理
        self.owner = ''  # 管理机构
        self.access = {}  # 基金评级
        self.rank = {  # 基金排行
            '3M': 0,
            '6M': 0,
            '1Y': 0,
            '2Y': 0,
            '3Y': 0,
            '5Y': 0,
        }
        self.up_down = {
            '3M': 0,
            '6M': 0,
            '1Y': 0,
            '2Y': 0,
            '3Y': 0,
            '5Y': 0,
            'until_now': 0,
        }


class Money(Fund):
    def __init__(self):
        ten_thousand_profit = 0
        seven_days_profit = 0


class Bond(Fund):
    pass


class Index(Fund):
    pass


class stock(Fund):
    pass


class Manager(scrapy.item):
    pass


class FundAgency(scrapy.Item):
    pass
