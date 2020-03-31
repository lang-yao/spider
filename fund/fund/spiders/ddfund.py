# -*- coding: utf-8 -*-
import scrapy


class DdfundSpider(scrapy.Spider):
    name = 'ddfund'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']

    def parse(self, response):
        pass
