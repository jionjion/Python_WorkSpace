# -*- coding: utf-8 -*-
'''
    ODM 对象文档模型
       pip install MongoEngine
       doc : http://docs.mongoengine.org/
'''

from mongoengine import Document
from mongoengine import StringField
from mongoengine import IntField
from mongoengine import DateTimeField
from mongoengine import connect


# 定义类型      Document:文档类型    EmbeddedDocument:嵌套的文档类型
class News(Document):
    title = StringField(max_length=200,required=True)
    content = StringField(max_length=2000,required=True)
    type = StringField(max_length=100,required=True)
    image = StringField(max_length=200,)
    author = StringField(max_length=2000)
    view_count = IntField()
    create_date = DateTimeField()
    is_valid = IntField()

    # 元数据,配置数据连接属性
    meta = {
        # 连接文档表名
        'collection' : 'news'
    }

class DML(object):

    # 创建连接
    def __init__(self):
        self.connect = connect('python', host='127.0.0.1', port=27017)


    # 新增一条数据
    def add_one(self):
        new = News(
            title='深夜好文',
            content='我们都知道自己是怎么一步一步落后于别人的',
            type='读书',
            author='Jion',
            create_date='2018-03-08 19:33:50'
        )
        # 直接保存
        new.save()
        return new

    # 查询一条数据
    def get_one(self):
        # 查询结果集中的第一个
        return News.objects.first()

    # 查询所有数据
    def get_all(self):
        # 查询结果集中的第一个
        return News.objects.all()

    # 通过id,查询数据,返回是一个结果集,如果不满足条件,则抛出异常,这里主动捕获,返回为空
    def get_id(self,id):
        try:
            return News.objects.filter(pk=id)
        except:
            # 未找到,返回空
            return None

    # 修改
    def modify_one(self):
        # 使用set__字段名 修改字符字段 , 使用 inc__字段名 修改数字字段
        result = News.objects.filter(title = '震惊,某男子深夜竟然做这种事').update(set__title='震惊,')
        return result

    # 删除
    def delete_one(self):
        # 删除第一条记录,如果没有first()则删除全部数据
        result = News.objects.filter(author='Jion').first().delete()
        # 返回删除的数量
        return result

if __name__ == '__main__':
    obj = DML()
    # print(obj.add_one().id)     # 通过 .[属性] 获得属性信息
    # print(obj.get_one().id)     # 获得id属性
    # print(obj.get_all())          # 获得所有的属性
    # print(obj.get_id('5aa4ce25041efcdbed1117f4'))
    # print(obj.modify_one())
    print(obj.delete_one())