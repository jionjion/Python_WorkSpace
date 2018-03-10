# -*- coding: utf-8 -*-

'''
    对数据进行删除操作
'''

import MySQLdb
# 创建类,并集成自父类
class MysqlDetele(object):

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

    # 修改一条记录
    def delete_one(self,id):
        try:
            # 使用元组,将过于长的字符包裹,默认SQL参数只支持字符串类型
            sql = "delete from `news` where `id` = %s"
            # 获取数据库连接
            cursor = self.conn.cursor()
            # 注意,当为一个元素时,添加逗号,构成一个元组
            cursor.execute(query=sql,args=(id,))
            # 提交事务
            self.conn.commit()
        except:
            # 一定要有异常捕获,避免事务部分失效,部分提交
            self.conn.rollback()
        finally:
            # 关闭连接
            cursor.close()
            self.conn.close()


if __name__ == '__main__':
    obj = MysqlDetele()
    obj.delete_one(10)