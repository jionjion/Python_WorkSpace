# -*- coding: utf-8 -*-

# Scrapy settings for ArticleSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import os

BOT_NAME = 'ArticleSpider'

SPIDER_MODULES = ['ArticleSpider.spiders']
NEWSPIDER_MODULE = 'ArticleSpider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ArticleSpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'ArticleSpider.middlewares.ArticlespiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# 请求和响应互联网时经过的中间件,数字越小越先执行,如果要重写,要么其执行顺序在系统的之后(数字填大点),或者将系统的注释或置None
DOWNLOADER_MIDDLEWARES = {
   'ArticleSpider.middlewares.RandomUserAgentMiddleWare': 543,
   'ArticleSpider.middlewares.ArticlespiderDownloaderMiddleware': None
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# 设置ORM映射模型的位置, 处理类 和 进入顺序,越小优先级越高,先处理图片,再处理保存
ITEM_PIPELINES = {
   # 框架生成的
   # 'ArticleSpider.pipelines.ArticlespiderPipeline': 300,
   # 自定义的图片下载
   # 'ArticleSpider.pipelines.ArticleImagesPipeline': 200,
   # 自定义的JSON写入
   # 'ArticleSpider.pipelines.JsonWithEncodingPipeline': 200,
   # 自定义的JSON导出
   # 'ArticleSpider.pipelines.JsonExporterPipleline': 200,
   # 自定义的MySQL存入
   # 'ArticleSpider.pipelines.MysqlPipeline': 200,
   # 使用异步连接池存入MySQL
   'ArticleSpider.pipelines.MysqlTwistedPipline': 200,

   # 'scrapy.pipelines.images.ImagesPipeline': 200,
}

# 图片下载配置 , 配置下载图片的文件路径和保存路径
IMAGES_URLS_FIELD = 'front_image_url'
project_dir = os.path.abspath(os.path.dirname(__file__))
IMAGES_STORE = os.path.join(project_dir,'images')
# 设定最大图片尺寸
# IMAGES_MIN_HEIGHT = 100
# IMAGES_MIN_WIDTH = 100

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 自定义,MySQL配置
MYSQL_HOST = '127.0.0.1'
MYSQL_DBNAME = 'scrapy'
MYSQL_PORT = 3306
MYSQL_USERNAME = 'root'
MYSQL_PASSWORD = '123456'

# 自定义,设置User-Agent,默认为Scrapy
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36';

# 自定义设置User-Agent的List
USER_AGENT_LIST = [
   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
   'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
   'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)'
]
# 使用第三方插件.fake-useragent并为其设置随机获取UserAgent的方式
USER_AGENT_TYPE = 'random'

# 设置项目路径,将当前项目作为资源目录
# sys.path.insert(0,"F:\PYTHON_WorkSpace\ArticleSpider\ArticleSpider")
import sys
sys.path.insert(0,os.path.join(project_dir,"ArticleSpider"))
