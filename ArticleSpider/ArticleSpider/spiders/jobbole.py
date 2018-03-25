# -*- coding: utf-8 -*-
import scrapy
'''
    爬取网站 http://blog.jobbole.com/all-posts/
'''

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'                            # 爬行项目的名字,用以调用项目
    allowed_domains = ['blog.jobbole.com']      # 开始网址
    start_urls = ['http://blog.jobbole.com/']   # 遍历的文件

    def parse(self, response):
        pass