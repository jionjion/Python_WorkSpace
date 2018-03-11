# -*- coding: utf-8 -*-
'''
    使用pymongo操作数据库
        pip install pymongo
        doc http://api.mongodb.com/python/
'''

import pymongo

# 创建客户端
client = pymongo.MongoClient("localhost", 27017)

# 地址
print(client.HOST)
# 端口
print(client.PORT)


# 现有数据列表
print(client.database_names())

# 连接数据库
db = client.python

# 数据库名称
print(db.name)


# 关闭,默认携带线程池,无需强制关闭
client.close()
