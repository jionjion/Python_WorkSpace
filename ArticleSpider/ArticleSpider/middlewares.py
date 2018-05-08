# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from fake_useragent import UserAgent


class ArticlespiderSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ArticlespiderDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

'''
    各种使用中用到的中间件
'''
class RandomUserAgentMiddleWare(object):
    # 随机更换请求头中的 User-Agent 参数

    def __init__(self, crawler):
        # 使用父类的方法,进行初始化
        super(RandomUserAgentMiddleWare, self).__init__()
        # 方式一:直接在settings配置文件中指定
        # 方式二: 获得settings中设置的USER_AGENT_LIST
        # self.user_agent_list = crawler.settings.get('USER_AGENT_LIST', [])
        # 方式三: 使用开源工具,获得其实例,需要提前下载
        self.userAgent = UserAgent()
        # 获得配置中的USER_AGENT_TYPE参数,(区分大小写),默认为random
        self.user_agent_type = crawler.settings.get('USER_AGENT_TYPE', 'random')

    @classmethod
    def from_crawler(cls, crawler):
        # 静态方法,从crawler获得请求内容
        return cls(crawler)

    def process_request(self, request, spider):
        # 匿名函数
        def get_ua():
            # 闭包特性,getattr(),获得某个对象的某个属性/方法. 相当于执行userAgent.user_agent_type()方法
            return getattr(self.userAgent, self.user_agent_type)

        # 随机获得一个UserAgent
        request.headers.setdefault('User_Agent', get_ua())
        # 设置IP代理.从http://www.xicidaili.com/nn中免费获取
        request.meta["proxy"] = "http://106.110.34.27:61234"
