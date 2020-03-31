# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from fund.items import *


class FundPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, Money):
            return item
        elif isinstance(item, Bond):
            return item
        elif isinstance(item, Index):
            return item
        elif isinstance(item, Stock):
            return item
        else:
            return item
