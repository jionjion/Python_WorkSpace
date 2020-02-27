# -*- coding: utf-8 -*-

###
#    通过 MySQLdb 模块实现
#        Mysql 的相关操作.
###
import MySQLdb
import datetime


class MysqlConnect:
    """
        连接MySQL数据库
    """

    # 创建数据库连接
    def get_connect(self):
        try:
            conn = MySQLdb.connect(
                host='127.0.0.1',
                user='root',
                passwd='123456',
                db='python',
                port=3306,
                charset='utf8'
            )
            return conn

        # 异常处理
        except MySQLdb.Error as e:
            # 打印异常
            print('Error: (%s)' % (e,))

    # 关闭连接
    def close_connect(self, conn):
        conn.close()


class MysqlConnectTest:
    """
        测试连接数据库类
    """
    if __name__ == '__main__':
        obj = MysqlConnect()
        # 获得连接
        conn = obj.get_connect()
        # 关闭连接
        obj.close_connect(conn)


class MysqlSelect:
    """
        查询语句
    """

    # 在类初始化时,创建连接绑定在对象参数中
    def __init__(self):
        # 调用获得连接方法
        try:
            # 绑定连接到对象参数中
            self.conn = MySQLdb.connect(
                host='127.0.0.1',
                user='root',
                passwd='123456',
                db='python',
                port=3306,
                charset='utf8'
            )
        except MySQLdb.Error as e:
            print('Error: (%s)' % (e,))

    # 关闭连接,如果连接存在
    def close_conn(self):
        try:
            if self.conn:
                self.conn.close()
        except MySQLdb.Error as e:
            print('Error: (%s)' % (e,))

    # 通过主键ID查询
    def get_one(self, book_id):
        # 准备SQL
        sql = 'select * from book where id = %s'
        # 生成游标
        cursor = self.conn.cursor()
        # 执行SQL,传入参数元组
        cursor.execute(query=sql, args=(book_id,))
        # 对结果处理,使用推导式,对记录进行键值对匹配
        result = dict(zip([k[0] for k in cursor.description], cursor.fetchone()))
        # 关闭游标连接,数据库连接
        cursor.close()
        # self.close_conn()
        # 返回结果
        return result

    # 字符条件查询,
    def get_column(self, book_name):
        # 通过反引号,标识这是一个表字段名或者表名
        sql = 'select * from `book` where `name` = %s'
        cursor = self.conn.cursor()
        cursor.execute(query=sql, args=(book_name,))
        result = [dict(zip([k[0] for k in cursor.description], row)) for row in cursor.fetchall()]
        cursor.close()
        # self.close_conn()
        return result

    # 模糊查询
    def get_like(self, book_name):
        sql = "select * from `book` where `name` like %s"
        cursor = self.conn.cursor()
        # 使用%%表示百分号,并被单引号包裹,进行模糊查询
        cursor.execute(query=sql, args=('%' + book_name + '%',))
        result = [dict(zip([k[0] for k in cursor.description], row)) for row in cursor.fetchall()]
        cursor.close()
        # self.close_conn()
        return result

    # 范围查询
    def get_in(self, id_list):
        sql = 'select * from `book` where `id` in %s'
        cursor = self.conn.cursor()
        # 传入一个列表元组
        cursor.execute(query=sql, args=(id_list,))
        result = [dict(zip([k[0] for k in cursor.description], row)) for row in cursor.fetchall()]
        cursor.close()
        # self.close_conn()
        return result

    # 日期查询
    def get_date(self, date_from, date_to):
        sql = "select * from `book` where `publication_date` between %s and %s"
        cursor = self.conn.cursor()
        # 日期查询直接将日期格式化后传入
        cursor.execute(query=sql, args=(date_from, date_to))
        result = [dict(zip([k[0] for k in cursor.description], row)) for row in cursor.fetchall()]
        cursor.close()
        # self.close_conn()
        return result

    # 分页查询
    def get_page(self, page, page_size):
        # 起始条数,和偏移量
        sql = "select * from `book` limit %s , %s"
        cursor = self.conn.cursor()
        # (当前页-1) * 每页数量 , 偏移量
        cursor.execute(query=sql, args=((page - 1) * page_size, page_size))
        result = [dict(zip([k[0] for k in cursor.description], row)) for row in cursor.fetchall()]
        cursor.close()
        # self.close_conn()
        return result


# 测试
class MysqlSelectTest:
    """
        测试查询
    """
    if __name__ == '__main__':
        obj = MysqlSelect()
        # 通过主键查询
        print("主键查询>> ", obj.get_one(1))
        # 通过字段查询
        print("字段查询>>", obj.get_column('三体'))
        # 通过模糊查询
        print("模糊查询>>", obj.get_like('三'))
        # 通过范围查询
        print("范围查询>>", obj.get_in([1, 2]))
        # 通过日期范围查询
        print("日期查询>>", obj.get_date('1000-01-01', '3000-01-01'))
        # 通过分页查询
        print("分页查询>>", obj.get_page(1, 1))
        # 关闭连接
        obj.close_conn()


# 增删改
class MysqlDML:
    """
        增删改动作
    """

    # 在类初始化时,创建连接绑定在对象参数中
    def get_conn(self):
        # 调用获得连接方法
        try:
            # 绑定连接到对象参数中
            conn = MySQLdb.connect(
                host='127.0.0.1',
                user='root',
                passwd='123456',
                db='python',
                port=3306,
                charset='utf8'
            )
            return conn
        except MySQLdb.Error as e:
            print('Error: %s' % e)

    # 关闭连接,如果连接存在
    def close_conn(self, conn):
        try:
            if conn:
                conn.close()
        except MySQLdb.Error as e:
            print('Error: %s' % e)

    # 新增一条记录
    def add_one(self):
        conn = None
        cursor = None
        try:
            # 使用元组,将过于长的字符包裹,默认SQL参数只支持字符串类型
            sql = ("insert into `book`(`name`,`author`,`publication_date`) "
                   "value (%s, %s, %s)")
            # 获取数据库连接
            conn = self.get_conn()
            cursor = conn.cursor()
            # 获取当前时间
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute(query=sql, args=('冰与火之歌', '乔治·马丁', now))
            # 提交事务
            conn.commit()
        except MySQLdb.Error:
            # 一定要有异常捕获,避免事务部分失效,部分提交
            conn.rollback()
        finally:
            # 关闭连接
            cursor.close()
            self.close_conn(conn)

    # 新增多条记录
    def add_more(self):
        conn = None
        cursor = None
        try:
            # 使用元组,将过于长的字符包裹,默认SQL参数只支持字符串类型
            sql = ("insert into `book`(`name`,`author`,`publication_date`) "
                   "values (%s, %s, %s)")
            # 获取数据库连接
            conn = self.get_conn()
            cursor = conn.cursor()
            # 获取当前时间
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # 批量数据,使用列表封装元组数据
            data = [('冰与火之歌', '乔治·马丁', now), ('三体', '刘慈宁', now)]
            cursor.executemany(query=sql, args=data)
            # 提交事务
            conn.commit()
        except MySQLdb.Error:
            # 一定要有异常捕获,避免事务部分失效,部分提交
            conn.rollback()
        finally:
            # 关闭连接
            cursor.close()
            self.close_conn(conn)

    # 修改一条记录
    def modify_one(self, book_id):
        conn = None
        cursor = None
        try:
            # 使用元组,将过于长的字符包裹,默认SQL参数只支持字符串类型
            sql = "update `book` set publication_date = %s where `id` = %s"
            # 获取数据库连接
            conn = self.get_conn()
            cursor = conn.cursor()
            # 获取当前时间
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute(query=sql, args=(now, book_id))
            # 提交事务
            conn.commit()
        except MySQLdb.Error:
            # 一定要有异常捕获,避免事务部分失效,部分提交
            conn.rollback()
        finally:
            # 关闭连接
            cursor.close()
            self.close_conn(conn)

    #  删除一条记录
    def delete_one(self, book_id):
        conn = None
        cursor = None
        try:
            # 使用元组,将过于长的字符包裹,默认SQL参数只支持字符串类型
            sql = "delete from `book` where `id` = %s"
            # 获取数据库连接
            conn = self.get_conn()
            cursor = conn.cursor()
            # 注意,当为一个元素时,添加逗号,构成一个元组
            cursor.execute(query=sql, args=(book_id,))
            # 提交事务
            conn.commit()
        except MySQLdb.Error:
            # 一定要有异常捕获,避免事务部分失效,部分提交
            conn.rollback()
        finally:
            # 关闭连接
            cursor.close()
            self.close_conn(conn)


# 增删改
class MysqlDMLTest:
    """
        测试增删改动作
    """
    if __name__ == '__main__':
        obj = MysqlDML()
        obj.add_one()
        obj.add_more()
        obj.modify_one(2)
        obj.delete_one(1)
