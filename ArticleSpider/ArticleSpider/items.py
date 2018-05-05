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
from scrapy.loader import ItemLoader

'''
    使用item类,将需要保存的对象放置到类中,实现orm映射保存
'''



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

# 自定义item_loader
class ArticleItemLoader(ItemLoader):
    # 重写默认的输出函数,不返回迭代器,而直接返回第一个元素
    default_output_processor = TakeFirst()


class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass



'''
    拉勾网爬取用到的类
'''
class LagouJob(scrapy.Item):
    # 拉勾网职位信息
    # 职位URL
    url = scrapy.Field()
    # 职位页面ID
    url_object_id = scrapy.Field()
    # 标题
    titile = scrapy.Field()
    # 薪资
    salary = scrapy.Field()
    # 工作地点
    job_city = scrapy.Field()
    # 工作年限
    work_year = scrapy.Field()
    # 学历要求
    degree_need = scrapy.Field()
    # 工作类型
    job_type = scrapy.Field()
    # 发布时间
    pulish_time = scrapy.Field()
    # 标签
    tag = scrapy.Field()
    # 职位诱惑
    job_advantage = scrapy.Field()
    # 职位描述
    job_desc = scrapy.Field()
    # 公司URL
    company_url = scrapy.Field()
    # 公司名
    company_name = scrapy.Field()
    # 创建时间
    crawl_time = scrapy.Field()
    # 最后更新时间
    crawl_update_tiem = scrapy.Field()