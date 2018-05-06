# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import datetime
import re

from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import TakeFirst
from scrapy.loader.processors import Join
from scrapy.loader import ItemLoader

from w3lib.html import remove_tags

'''
    使用item类,将需要保存的对象放置到类中,实现orm映射保存
'''
class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


# 日期转为字符
def date_to_str(value):
    try:
        value = datetime.datetime.strptime(value, '%Y/%m/%d')
    except Exception as e:
        value = datetime.datetime.now().date()
    return value


# 获得字符中的数字
def get_number(value):
    # 获得内容中的数字部分,不匹配为0
    value = re.match(r'.*?(\d+).*', value)
    if value:
        value = int(value.group(1))
    else:
        value = 0
    return value


# 返回原值
def return_value(value):
    return value

# 创建文章对象类,继承自scrapy.Item父类
class JobboleArticleItem(scrapy.Item):
    # 主键,对URL摘要,便于去重
    object_url_id = scrapy.Field()
    # 标题,类型为Field()类型
    title = scrapy.Field(
        # 对传入字段进行预处理,传入多个函数,依次对数据进行处理
    )
    # 封面
    front_image_url = scrapy.Field(
        # 使用return_value,在不改变原来返回值的基础上,覆盖default_output_processor,使其返回一个数组,让框架下载对应图片
        output_processor = MapCompose(return_value),
    )
    front_image_path = scrapy.Field()
    # 创建日期
    create_date = scrapy.Field(
        input_processor = MapCompose(date_to_str),
        # 只返回第一个元素,避免传入数组
        output_processor = TakeFirst()
    )
    # 链接
    url = scrapy.Field()
    # 点赞
    thumb_num = scrapy.Field(
        input_processor = MapCompose(get_number),
    )
    # 收藏
    mark_num = scrapy.Field(
        input_processor=MapCompose(get_number),
    )
    # 内容
    content = scrapy.Field()

    # 入库SQL,作为item的方法的返回
    def get_insert_sql(self):
        insert_sql = """
            insert into jobbole_article(
                    object_url_id, title, front_image_url, front_image_path,
                    create_date , url , thumb_num , mark_num , content)
            values (%s, %s, %s, %s, %s, %s, %s, %s, %s) 
            on duplicate key 
            update content=values(content)
        """
        # fron_image_url = ""
        # content = remove_tags(self["content"])

        # if self["front_image_url"]:
        #     fron_image_url = self["front_image_url"][0]
        params = (self["object_url_id"], self["title"], self["front_image_url"], self["front_image_path"],
                  self["create_date"], self["url"], self["thumb_num"], self["mark_num"], self["content"])
        # 返回SQL和参数列表
        return insert_sql, params

# 自定义item_loader
class ArticleItemLoader(ItemLoader):
    # 重写默认的输出函数,不返回迭代器,而直接返回第一个元素
    default_output_processor = TakeFirst()




'''
    拉勾网爬取用到的类
'''

# 拉勾网自定义的迭代器,返回选择器匹配到的第一个,而不是一个数组
class LagouItemLoader(ItemLoader):
    default_output_processor = TakeFirst()

# 删除两侧的/
def remove_splash(value):
    return value.replace('/','')

# 专门处理工作地点字段,去除换行和空格
def handle_jobaddr(value):
    addr_list = value.split('\n')
    addr_list = [item.strip() for item in addr_list if item.strip()!='查看地图']
    return "".join(addr_list)

class LagouJobItem(scrapy.Item):
    # 拉勾网职位信息
    # 职位URL
    url = scrapy.Field()
    # 职位页面ID
    url_id = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 薪资
    salary = scrapy.Field()
    # 工作地点
    job_city = scrapy.Field(
        # 删除两侧/斜线
        input_processor = MapCompose(remove_splash),
    )
    # 工作年限
    work_year = scrapy.Field(
        input_processor = MapCompose(remove_splash),
    )
    # 学历要求
    degree_need = scrapy.Field(
        input_processor = MapCompose(remove_splash),
    )
    # 工作类型
    job_type = scrapy.Field(
        input_processor = MapCompose(remove_splash),
    )
    # 发布时间
    publish_time = scrapy.Field()
    # 标签
    tag = scrapy.Field(
        # 逗号间隔,标签组合输出
        output_processor=Join(",")
    )
    # 职位诱惑
    job_advantage = scrapy.Field()
    # 职位描述
    job_desc = scrapy.Field()
    # 工作地址
    job_addr = scrapy.Field(
        # 去除Html标签
        input_processor=MapCompose(remove_tags,handle_jobaddr)

    )
    # 公司URL
    company_url = scrapy.Field()
    # 公司名
    company_name = scrapy.Field()
    # 创建时间
    crawl_time = scrapy.Field()
    # 最后更新时间
    crawl_update_time = scrapy.Field()

    # 编写SQL语句, 方法名约定get_insert_sql,便于在pipelines中通用调用
    def get_insert_sql(self):
        insert_sql = """
            insert into lagou_job (
                url_id, url,  title,  salary, job_city,
                work_year,  degree_need,  job_type, publish_time,
                tag,  job_advantage,  job_addr, job_desc, company_url,
                company_name)
            values(
                %s, %s, %s, %s, %s,
                %s, %s, %s, %s,
                %s, %s, %s, %s, %s,  
                %s)
            on duplicate key 
            update salary = values(salary) , job_desc = values(job_desc)
        """
        params = (
            self["url_id"], self["url"], self["title"], self["salary"], self["job_city"],
            self["work_year"], self["degree_need"], self["job_type"], self["publish_time"],
            self["tag"],self["job_advantage"], self["job_addr"], self["job_desc"], self["company_url"],
            self["company_name"],
        )
        return insert_sql, params



