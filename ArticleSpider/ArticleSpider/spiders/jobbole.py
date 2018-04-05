# -*- coding: utf-8 -*-
import scrapy
import re
'''
    爬取网站 http://blog.jobbole.com/all-posts/
'''

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'                            # 爬行项目的名字,用以调用项目
    allowed_domains = ['blog.jobbole.com']      # 开始网址
    start_urls = ['http://blog.jobbole.com/110287/']   # 遍历的文件

    def parse(self, response):
        # 爬取任何节点,class为id,值为post-110287的元素下的第一个div的h1标签,获取元素的值,调用text()函数,获得一个 Selector对象
        title_selector = response.xpath('//*[@id="post-110287"]/div[1]/h1/text()')
        # 调用 Selector对象的extract()方法,获得爬取的文字信息,返回一个数组
        print(title_selector[0].extract())
        # 获得创建时间
        create_date =response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()')[0].extract().strip().replace('·', '').strip()
        print(create_date)

        # 获得点赞数         # contains(属性,包含属性值) 内置函数,搜索属性值匹配的函数
        thumb_num = int(response.xpath('//span[contains(@class,"vote-post-up")]/h10/text()')[0].extract()[0])
        print(thumb_num)

        # 获得收藏数
        mark_num = response.xpath('//span[contains(@class,"bookmark-btn")]/text()')[0].extract()
        # 获得内容中的数字部分
        mark_num = int ( re.match(r'.*(\d+).*',mark_num).group(1) )
        print(mark_num)

        # 获得正文,包含各种标签,换行
        content = response.xpath('//div[@class="entry"]').extract()
        print(content)
