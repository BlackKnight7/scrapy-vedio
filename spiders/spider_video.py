# -*- coding: utf-8 -*-
import scrapy

class VedioSpider(scrapy.Spider):
    name = 'vediospider'
    start_urls = ['http://www.imooc.com/video/10688']

    def parse(self, response):
        for url in response.css('ul li a::attr("href")').re('.*/category/.*'):
            yield scrapy.Request(response.urljoin(url), self.parse_titles)