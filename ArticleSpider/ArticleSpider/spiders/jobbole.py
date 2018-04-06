# -*- coding: utf-8 -*-
import re
import time
import datetime
from urllib import parse

import scrapy
from ArticleSpider.items import JobboleArticleItem  # 这里由于设定了项目根目录,以ArticleSpider所在文件为根目录
from ArticleSpider.items import ArticleItemLoader
from ArticleSpider.utils.commons import get_md5
from scrapy.http import Request
from scrapy.loader import ItemLoader

'''
    爬取网站 http://blog.jobbole.com/all-posts/
'''

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'                            # 爬行项目的名字,用以调用项目
    allowed_domains = ['blog.jobbole.com']      # 开始网址
    start_urls = ['http://blog.jobbole.com/all-posts/']   # 遍历的文件

    # 解析列表页面信息
    def parse(self, response):
        # 获取当前页的全部文章的URL,交由解析
        post_nodes = response.css("#archive .floated-thumb .post-thumb a")
        for post_node in post_nodes:
            # 使用URL拼接,将前者的域名与后者的项目路径做拼接
            url = parse.urljoin(base=response.url , url=post_node.css("::attr(href)").extract_first(""))
            # 获取图片URL
            img_url = post_node.css("img ::attr(src)").extract_first("")
            # 避免url中,只有行对路径
            img_url = parse.urljoin(base=response.url , url=img_url)
            # 请求并调用回调函数   meta,异步调用时,需要的参数,将参数传入parse_deteil解析函数  yield 关键字,返回交给框架解析
            yield Request(url=url,meta={"front_image_url":img_url},callback=self.parse_deteil)

        # 获取下一页的URL,并交由框架解析, 两个类相邻表示获取具有的两个类的元素
        next_url = response.css(".next.page-numbers ::attr(href)").extract_first("")
        # 存在,交由爬取
        if next_url:
            url = parse.urljoin(base=response.url, url=next_url)
            # 请求,并调用parse函数,继续获得页面的文章所有的URL
            yield Request(url=url,callback=self.parse)

    # 解析文章的具体信息
    def parse_deteil(self,response):
        # 获得传入的meta对象的front_image_url值,文章封面
        front_image_url = response.meta.get("front_image_url","")
        # 爬取任何节点,class为entry-header的元素下的第一个div的h1标签,获取元素的值,调用text()函数,获得一个 Selector对象
        title_selector = response.css('.entry-header h1 ::text')
        # 调用 Selector对象的extract()方法,获得爬取的文字信息,返回一个数组
        title = title_selector[0].extract()
        # 获得创建时间
        create_date =response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()')[0].extract().strip().replace('·', '').strip()

        # 获得点赞数         # contains(属性,包含属性值) 内置函数,搜索属性值匹配的函数
        thumb_num = int(response.xpath('//span[contains(@class,"vote-post-up")]/h10/text()')[0].extract()[0])

        # 获得收藏数
        mark_num = response.xpath('//span[contains(@class,"bookmark-btn")]/text()')[0].extract()
        # 获得内容中的数字部分,不匹配为0
        mark_num = re.match(r'.*?(\d+).*',mark_num)
        if mark_num:
            mark_num = int( mark_num.group(1) )
        else:
            mark_num = 0

        # 获得正文,包含各种标签,换行
        content = response.xpath('//div[@class="entry"]').extract()

        # 实例化对象
        article_item = JobboleArticleItem()
        # 赋值
        article_item["object_url_id"] = get_md5(response.url)
        article_item["title"] = title
        article_item["front_image_url"] = [front_image_url]
        try:
            article_item["create_date"] = datetime.datetime.strptime(create_date,'%Y/%m/%d')
        except Exception as e:
            article_item["create_date"] = datetime.datetime.now().date()
        article_item["url"] = response.url
        article_item["thumb_num"] = thumb_num
        article_item["mark_num"] = mark_num
        article_item["content"] = content

        '''
            使用ItemLoader,定义解析规则
        '''
        item_loader = ArticleItemLoader(item=JobboleArticleItem(),response=response)
        item_loader.add_value(field_name="object_url_id",value=get_md5(response.url))
        item_loader.add_css(field_name="title",css=".entry-header h1 ::text")
        item_loader.add_value(field_name="front_image_url",value=front_image_url)
        item_loader.add_xpath(field_name="create_date", xpath= "//p[@class='entry-meta-hide-on-mobile']/text()")
        item_loader.add_value(field_name="url",value=response.url)
        item_loader.add_xpath(field_name="thumb_num", xpath= "//span[contains(@class,'vote-post-up')]/h10/text()")
        item_loader.add_xpath(field_name="mark_num" , xpath= "//span[contains(@class,'bookmark-btn')]/text()")
        item_loader.add_xpath(field_name="content", xpath= "//div[@class='entry']")
        # 解析规则,返回对象
        article_item = item_loader.load_item()

        # 传递
        yield article_item

