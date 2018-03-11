# -*- coding: utf-8 -*-

from pymongo import MongoClient
from bson.objectid import ObjectId

class mongodbModify(object):
    # 重写初始化方法,为调用对象新增属性
    def __init__(self):
        # 实例化一个接连
        self.client = MongoClient()
        # 连接数据库
        self.db = self.client['python']

    # 更新一个  $set 针对字符串进行修改
    def modify_one(self):
        result = self.db.news.update_one({'title':'震惊!'},{'$set':{'title':'震惊!某男子深夜竟然做这种事'}})
        print('匹配行数>>' + str(result.matched_count))
        print('修改行数>>' + str(result.modified_count))

    # 更新多个  $inc 针对数字进行修改
    def modify_many(self):
        result = self.db.news.update_many({},{'$set':{'author':'Jion'}})
        print('匹配行数>>' + str(result.matched_count))
        print('修改行数>>' + str(result.modified_count))

if __name__ == '__main__':
    obj = mongodbModify()
    obj.modify_one()
    # obj.modify_many()