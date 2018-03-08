# -*- coding: utf-8 -*-

'''
    mysqlclient 方法类
'''

import MySQLdb

# 创建类,并集成自父类
class MysqlSearch(object):

    # 在类初始化时,创建连接绑定在对象参数中
    def __init__(self):
        self.get_conn()

    # 数据库连接方法
    def get_conn(self):
        try:
            # 将方法返回值直接挂载到调用对象中
            self.conn = MySQLdb.connect(
                host='127.0.0.1',
                user='root',
                passwd='123456',
                db='python',
                port=3306,
                charset='utf8'
            )
        # 异常处理
        except MySQLdb.Error as e:
            # 打印异常
            print('Error: %s' % e)

    # 如果存在,则关闭连接
    def close_conn(self):
        try:
            if self.conn:
                self.conn.close()
        except MySQLdb.Error as e:
            print('Error: %s' % e)


    # 查询方法
    def get_one(self,id):
        # 准备SQL
        sql = 'select * from news where id = %s'
        # 生成游标
        cursor = self.conn.cursor()
        # 执行SQL,传入参数元组
        cursor.execute(query=sql,args=(id,))
        # 对结果处理,使用推导式,对记录进行键值对匹配
        result = dict(zip([k[0] for k in cursor.description] , cursor.fetchone()))
        # 关闭游标连接,数据库连接
        cursor.close()
        self.close_conn()
        # 返回结果
        return result

    # 查询方法
    def get_type(self,type):
        sql = 'select * from `news` where `type` = %s'
        cursor = self.conn.cursor()
        cursor.execute(query=sql,args=(type,))
        result = [dict(zip([k[0] for k in cursor.description],row))for row in cursor.fetchall()]
        return result

    # 分页查询

    # 插入


    # 修改

    # 删除

# 注意缩进,main方法不在类方法内
if __name__ == '__main__':
    obj = MysqlSearch()
    print(obj.get_type('读书'))


