# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from items import LagouItemLoader, LagouJobItem
from utils.commons import get_md5
from datetime import datetime

'''
    全站爬取页面
'''
class LagouSpider(CrawlSpider):
    name = 'lagou'
    allowed_domains = ['www.lagou.com']
    start_urls = ['https://www.lagou.com/']

    # 请求设置,不启用Cookies,避免被拦截
    custom_settings = {
        "COOKIES_ENABLED": False,
        "DOWNLOAD_DELAY": 1,
        'DEFAULT_REQUEST_HEADERS': {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Connection': 'keep-alive',
            'Cookie': '_ga=GA1.2.423832464.1525571709; _gid=GA1.2.1964943705.1525571709; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1525507738,1525570198,1525571668; LGSID=20180506095509-81f0f404-50d0-11e8-803d-5254005c3644; LGUID=20180506095509-81f0f6d3-50d0-11e8-803d-5254005c3644; PRE_HOST=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2F4420625.html; PRE_SITE=; PRE_UTM=; user_trace_token=20180506095509-63c4c57b-52c0-421e-bfa8-04f9d2bff302; JSESSIONID=ABAAABAAADEAAFIEE869A27A8071F47BE050D4A07B0DD92; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; LGRID=20180506095841-ffe31c38-50d0-11e8-87ee-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1525571921',
            'Host': 'www.lagou.com',
            'Origin': 'https://www.lagou.com',
            'Referer': 'https://www.lagou.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        }
    }

    # 详情页面的URL规则
    rules = (
        # 使用正则,爬取站点的URL规则,省略主域名  示例: https://www.lagou.com/jobs/4524082.html
        # callback 执行爬取页面的回调函数
        # follow 是否在此页面基础上下钻
        Rule(LinkExtractor(allow=r'jobs/\d+.html'), callback='parse_job', follow=True),

        # 列表页面的URL规则
        # 示例 https://www.lagou.com/zhaopin/
        Rule(LinkExtractor(allow=r'zhaopin/.*'),callback='',follow=True),

        # 公司页面的URL规则
        # 示例 https://www.lagou.com/gongsi/109.html
        Rule(LinkExtractor(allow=r'gongsi/\d+.html'), callback='', follow=True)

    )

    # 回调执行,解析职位详情页面
    def parse_job(self, response):
        # 创建对象加载器
        item_loader = LagouItemLoader(item=LagouJobItem(),response=response)
        # 标题
        item_loader.add_css(field_name="title", css=".job-name ::attr(title)")
        # URL
        item_loader.add_value(field_name="url", value=response.url)
        # URL摘要
        item_loader.add_value(field_name="url_id", value=get_md5(response.url))
        # 薪资
        item_loader.add_css(field_name="salary", css="span[class=salary] ::text")
        # 工作地点
        item_loader.add_xpath(field_name="job_city", xpath="//*[@class='job_request']/p/span[2]/text()")
        # 工作年限
        item_loader.add_xpath(field_name="work_year", xpath="//*[@class='job_request']/p/span[3]/text()")
        # 学历要求
        item_loader.add_xpath(field_name="degree_need", xpath="//*[@class='job_request']/p/span[4]/text()")
        # 工作类型
        item_loader.add_xpath(field_name="job_type", xpath="//*[@class='job_request']/p/span[5]/text()")
        # 标签
        item_loader.add_css(field_name="tag", css=".position-label li::text")
        # 发布时间
        item_loader.add_css(field_name="publish_time", css=".publish_time ::text")
        # 职位诱惑
        item_loader.add_css(field_name="job_advantage", css=".job-advantage p ::text")
        # 职位描述
        item_loader.add_css(field_name="job_desc", css=".job_bt div")
        # 工作地址
        item_loader.add_css(field_name="job_addr", css=".work_addr")
        # 公司名称
        item_loader.add_css(field_name="company_name", css="#job_company img::attr('alt')")
        # 公司主页
        item_loader.add_css(field_name="company_url", css="#job_company ul a::attr('href')")

        job_item = item_loader.load_item()
        # print(job_item)
        return job_item

