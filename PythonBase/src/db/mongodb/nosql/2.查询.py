# -*- coding: utf-8 -*-

from pymongo import MongoClient
from bson.objectid import ObjectId

class mongodbSearch(object):
    # 重写初始化方法,为调用对象新增属性
    def __init__(self):
        # 实例化一个接连
        self.client = MongoClient()
        # 连接数据库
        self.db = self.client['python']

    def get_one(self):
        # 根据id查询
        return self.db.news.find_one()

    def get_all(self):
        # 查询全部数据
        return self.db.news.find()

    def get_id(self,id):
        # 查询指定id的数据,需要将其转为ObjectId()类型
        oid = ObjectId(id)
        return self.db.news.find_one({'_id':oid})

if __name__ == '__main__':
    obj = mongodbSearch()
    # obj.get_one()['_id'] # 字典类型,记录的主键
    # for item in obj.get_all(): # 游标类型,可以使用for循环处理
    #     print(item)
    print(obj.get_id('5aa4a3c4dcc7d5c778ab379f'))