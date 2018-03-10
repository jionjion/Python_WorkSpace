# -*- coding: utf-8 -*-

'''
    对MySQL数据库执行插入操作
    单条插入
    批量插入
'''

import MySQLdb
import datetime
# 创建类,并集成自父类
class MysqlInsert(object):

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

    # 新增一条记录
    def add_one(self):
        try:
            # 使用元组,将过于长的字符包裹,默认SQL参数只支持字符串类型
            sql = ("insert into `news`(`title`,`content`,`type`,`image`,`author`,`view_count`,`create_date`,`is_valid`) "
                   "value (%s,%s,%s,%s,%s,%s,%s,%s)")
            # 获取数据库连接
            cursor = self.conn.cursor()
            # 获取当前时间
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute(query=sql,args=('就问你怕不怕','昨夜,上海地区温度跌破冰点,上海人表示受不了','新闻','','Jion', 1 , now, 1 ))
            # 提交事务
            self.conn.commit()
        except:
            # 一定要有异常捕获,避免事务部分失效,部分提交
            self.conn.rollback()
        finally:
            # 关闭连接
            cursor.close()
            self.conn.close()

    # 新增多条记录
    def add_more(self):
        try:
            # 使用元组,将过于长的字符包裹,默认SQL参数只支持字符串类型
            sql = ("insert into `news`(`title`,`content`,`type`,`image`,`author`,`view_count`,`create_date`,`is_valid`) "
                   "values (%s,%s,%s,%s,%s,%s,%s,%s)")
            # 获取数据库连接
            cursor = self.conn.cursor()
            # 获取当前时间
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # 批量数据,使用lsit列表封装元组数据
            datas = [('五分钟即可','每天抽出五分钟时间,读书看报聊人生','读书','','Jion', 1 , now, 1 )
                    ,('尴尬时刻,男默女泪','降温了,但是却没有衣服穿','新闻','','Jion', 1 , now, 1 )
                    ,('大动作,搞事情', '昨夜,读完了一本书', '读书', '', 'Jion', 1, now, 1)]
            cursor.executemany(query=sql,args=datas)
            # 提交事务
            self.conn.commit()
        except MySQLdb.Error as e:
            # 一定要有异常捕获,避免事务部分失效,部分提交
            self.conn.rollback()
        finally:
            # 关闭连接
            cursor.close()
            self.conn.close()

if __name__ == '__main__':
    obj = MysqlInsert()
    obj.add_more()