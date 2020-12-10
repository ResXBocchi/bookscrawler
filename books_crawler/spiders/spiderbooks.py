# -*- coding: utf-8 -*-
import scrapy


class SpiderbooksSpider(scrapy.Spider):
    name = 'spiderbooks'
    allowed_domains = ['http://books.toscrape.com']
    start_urls = ['http://http://books.toscrape.com/']

    def parse(self, response):
        pass
