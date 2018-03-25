工具方法
首先在 http://blog.jobbole.com/all-posts/ 这个网址中获得可以查询到所有的页面

## 创建项目 
    scrapy startproject ArticleSpider
创建一个新的空项目

## 文件说明
../spiders/             存放爬虫代码
./items.py              自定义数据类型
./middlewares.py        中间扩展软件
./pipelines.py          数据库储存
./settings.py           配置文件
scrapy.cfg              整体配置文件


## 爬取伯乐在线
在当前项目下,执行
    scrapy genspider jobbole blog.jobbole.com
会创建一个jobbole.py文件在spiders文件夹下

启动当前项目
    jobbolescrapy crawl jobbole

安装win32 
    pip install pypiwin32