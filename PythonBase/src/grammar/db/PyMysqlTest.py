import pymysql
import datetime


# 连接MySQL
class MysqlConnect:

    # 获取数据库连接
    def get_connect(self):
        conn = pymysql.Connect(host="127.0.0.1", user="root", password="123456",
                               database="python", port=3306, charset='utf8')
        return conn

    # 关闭连接
    def close_connect(self, conn):
        # 关闭连接
        conn.close()

    # 尝试获得数据
    def get_data(self):
        # 获得连接
        conn = self.get_connect()
        # 获得数据库游标,默认抓取的数据结构为元组类型
        cursor = conn.cursor()
        # SQL
        sql_select = "select * from `book`"
        # 执行查询,获得数据
        cursor.execute(sql_select)
        # 查看游标数据总数
        print("数据总数: %s" % (cursor.rowcount,))
        # 数据
        row_data = cursor.fetchall()
        print("数据: (%s)" % (row_data,))
        # 关闭游标
        cursor.close()
        # 关闭连接
        self.close_connect(conn)


# 测试连接MySQL
class MysqlConnectTest:
    if __name__ == '__main__':
        obj = MysqlConnect()
        obj.get_data()


# 查询
class MysqlSelect:
    # 获得连接
    def get_connect(self):
        conn = pymysql.Connect(host="127.0.0.1", user="root", password="123456",
                               database="python", port=3306, charset='utf8')
        return conn

    # 关闭连接
    def close_connect(self, conn):
        # 关闭连接
        conn.close()

    # 查询数据
    def get_rows(self):
        # 获得连接
        conn = self.get_connect()
        # 获得数据库游标,抓取的数据为JSON类型
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # SQL
        sql_select = "select * from `book`"
        # 执行查询,获得数据
        cursor.execute(sql_select)
        # 抓取一条记录
        rs = cursor.fetchone()
        print("抓取一条记录:", rs)
        # 抓取指定记录
        rs = cursor.fetchmany(2)
        print("抓取两条记录", rs)
        # 移动游标
        # 相对当前位置移动,向后移动1位
        cursor.scroll(1, mode='relative')
        # 相对绝对位置移动,移动到第二个位置,随后向后移动2位
        cursor.scroll(2, mode='absolute')
        # 抓取全部记录
        rs = cursor.fetchall()
        # 对抓取的数据进行解析,仅限于元组数据结构
        print("抓取剩余记录", rs)
        for row in rs:
            print("用户名:", row[1])
        # 关闭游标
        cursor.close()
        # 关闭连接
        self.close_connect(conn)


# 测试查询
class MysqlSelectTest:
    if __name__ == '__main__':
        obj = MysqlSelect()
        obj.get_rows()


# 事物
class MysqlTransaction:
    # 获得连接
    def get_connect(self):
        conn = pymysql.Connect(host="127.0.0.1", user="root", password="123456",
                               database="python", port=3306, charset='utf8')
        return conn

    # 关闭连接
    def close_connect(self, conn):
        # 关闭连接
        conn.close()

    # 事物操作
    def modify(self):
        # 事务开启,默认自动提交事务是关闭的.如果不执行commit操作,数据的增删改是不会发生改变的
        # 获得连接
        conn = self.get_connect()
        # 获得数据库游标,抓取的数据为JSON类型
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            # 增加记录
            sql_insert = "insert into `book`(name, author, publication_date) values ('三体', '刘慈宁', '2020-02-29 00:00:00')"
            cursor.execute(sql_insert)
            # 修改记录
            sql_update = "update `book` set author = '刘慈宁' where id = 2"
            cursor.execute(sql_update)
            # 删除记录
            sql_delete = "delete from `book` where id = 7"
            cursor.execute(sql_delete)
            print("单条删除影响的记录数", cursor.rowcount)
            # 执行预编译的sql,并返回影响的行数,s%为占位符
            effect_row = cursor.execute("update `book` set author = '刘慈宁' where id = %s", (2,))
            print("预编译更新影响的记录数", effect_row)
            # 获取当前时间
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data = [('冰与火之歌', '乔治·马丁', now), ('三体', '刘慈宁', now)]
            # 批量插入,传入list序列
            effect_row = cursor.executemany("insert into `book`(name, author, publication_date) values (%s, %s, %s)", data)
            print("批量插入影响的记录数", effect_row)
            # 获取自增ID,最后一条插入后的主键ID
            new_id = cursor.lastrowid
            print("最后一条记录主键ID:", new_id)
            # 事务提交
            conn.commit()
        except Exception as e:  # 如果出现异常,则回滚
            print("事务执行出现异常:", e)
            # 事务回滚
            conn.rollback()
        finally:
            # 关闭游标
            cursor.close()
            # 关闭连接
            conn.close()


# 测试事物
class MysqlTransactionTest:
    if __name__ == '__main__':
        obj = MysqlTransaction()
        obj.modify()
