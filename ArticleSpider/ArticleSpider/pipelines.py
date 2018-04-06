# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

'''
    类似于拦截器,将每个自定义item对象进行拦截
    通过设定优先级的不同,进而可以依次拦截处理爬取对象
'''

from scrapy.pipelines.images import ImagesPipeline
import codecs
import json
import os
from scrapy.exporters import JsonItemExporter
import MySQLdb
import MySQLdb.cursors
from twisted.enterprise import adbapi


# 数据储存的类
class ArticlespiderPipeline(object):
    # 数据储存的方法
    def process_item(self, item, spider):
        return item


# 将抓取结果,以JSON文件进行存储
class JsonWithEncodingPipeline(object):
    # 初始化方法,完成文件加载
    def __init__(self):
        # 文件路径
        file = os.path.dirname(__file__) + '/json/article.json'
        # 打开文件
        self.file = codecs.open(filename=file, mode='w', encoding='utf-8')

    # 写入文件的方法
    def process_item(self, item, spider):
        # 将item转为JSON结构,不启用union code编码
        lines = json.dumps(obj=dict(item), ensure_ascii=False) + '\n'
        self.file.write(lines)
        return item

    # 管道关闭方法
    def spider_closed(self, spider):
        self.file.close()


# 使用框架提供的导出方法,导出为JSON结构数据
class JsonExporterPipleline(object):
    def __init__(self):
        # 文件路径
        file = os.path.dirname(__file__) + '/json/articleExport.json'
        # 打开文件
        self.file = open(file=file, mode='wb')
        # 创建导出对象
        self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        # 执行导出
        self.exporter.start_exporting()

    # 写入文件的方法
    def process_item(self, item, spider):
        self.exporter.export_item(item=item)
        return item

    # 关闭导出
    def close_spider(self, spider):
        # 停止导出方法
        self.exporter.finish_exporting();
        self.file.close()


# 图片下载相关,重写父类的下载方法
class ArticleImagesPipeline(ImagesPipeline):
    # 重载下载图片的方法
    def item_completed(self, results, item, info):
        # 仅针对存在图片下载链接使用
        if "front_image_url" in item:
            for ok, value in results:
                # 获得图片的下载路径
                image_path = value['path']
            item['front_image_path'] = image_path
            return item


# 保存数据库的方法
class MysqlPipeline(object):
    # 初始化方法,创建连接和游标
    def __init__(self):
        self.conn = MySQLdb.connect(host='127.0.0.1',
                                    user='root',
                                    passwd='123456',
                                    db='scrapy',
                                    port=3306,
                                    charset='utf8',
                                    use_unicode=True)
        self.cursor = self.conn.cursor()

    # 保存方法
    def process_item(self, item, spider):
        insert_sql = '''
            insert into jobbole_article(object_url_id , title , front_image_url , front_image_path , 
                                          create_date , url , thumb_num , mark_num , content)
            values (%s , %s , %s , %s , %s , %s , %s , %s , %s)
        '''
        self.cursor.execute(query=insert_sql, args=(
        item["object_url_id"], item["title"], item["front_image_url"], item["front_image_path"],
        item["create_date"], item["url"], item["thumb_num"], item["mark_num"], item["content"]))
        # 提交,保存
        self.conn.commit()


# 使用连接池,将保存操作以异步方式提交
class MysqlTwistedPipline(object):

    # 重写构造函数,在创建对象时,完成赋值
    def __init__(self, dbpool):
        self.dbpool = dbpool

    # 读取settings.py配置文件中的信息,创建连接池
    @classmethod
    def from_settings(cls, settings):
        dbparms = dict(
            host=settings["MYSQL_HOST"],
            db=settings["MYSQL_DBNAME"],
            port=settings["MYSQL_PORT"],
            user=settings["MYSQL_USERNAME"],
            passwd=settings["MYSQL_PASSWORD"],
            charset="utf8",
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        # 创建连接池
        dbpool = adbapi.ConnectionPool("MySQLdb", **dbparms)
        # 返回连接池信息,调用构造函数,创建对象.
        return cls(dbpool)

    # 使用异步方式,完成数据插入
    def process_item(self, item, spider):
        # 执行异步方法
        query = self.dbpool.runInteraction(self.do_insert, item)
        # 添加异常处理回调
        query.addErrback(self.error_handler, item, spider)

    # 定义错误处理函数
    def error_handler(self, failure, item, spider):
        print(failure)

    # 保存方法,被异步调用,参数列表固定
    def do_insert(self, cursor, item):
        insert_sql = '''
            insert into jobbole_article(object_url_id , title , front_image_url , front_image_path , 
                                          create_date , url , thumb_num , mark_num , content)
            values (%s , %s , %s , %s , %s , %s , %s , %s , %s)
        '''
        cursor.execute(query=insert_sql,
                       args=(item["object_url_id"], item["title"], item["front_image_url"], item["front_image_path"],
                             item["create_date"], item["url"], item["thumb_num"], item["mark_num"], item["content"]))
        # 自动提交,保存
