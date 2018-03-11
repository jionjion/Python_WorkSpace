# -*- coding: utf-8 -*-

from pymongo import MongoClient
from bson.objectid import ObjectId

class mongodbDelete(object):
    # 重写初始化方法,为调用对象新增属性
    def __init__(self):
        # 实例化一个接连
        self.client = MongoClient()
        # 连接数据库
        self.db = self.client['python']

    # 删除一条,默认删除第一条
    def delete_one(self):
        result = self.db.news.delete_one({'title':'尴尬时刻'})
        print('删除行数>>' + str(result.deleted_count))

    # 删除多条
    def delete_many(self):
        result = self.db.news.delete_many({'author':'Jion'})
        print('删除行数>>' + str(result.deleted_count))

if __name__ == '__main__':
    obj = mongodbDelete()
    # obj.delete_one()
    obj.delete_many()