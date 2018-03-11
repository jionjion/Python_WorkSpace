# -*- coding: utf-8 -*-
from pymongo import MongoClient
from datetime import datetime

class mongodbInsert(object):
    # 重写初始化方法,为调用对象新增属性
    def __init__(self):
        # 实例化一个接连
        self.client = MongoClient()
        # 连接数据库
        self.db = self.client['python']

    # 新增一条数据
    def add_one(self):
        # 数据对象
        new = {
           'title':'尴尬时刻',
            'content':'降温了',
            'type':'新闻',
            'author':'Jion',
            'create_date': datetime.now()
        }
        # 插入数据
        return self.db.news.insert_one(new)


if __name__ == '__main__':
    obj = mongodbInsert()
    result = obj.add_one()
    print(result.inserted_id)