# -*- coding: utf-8 -*-

'''
    mysqlclient 连接MySQL
'''

import MySQLdb


# 创建数据库连接
try:
    conn = MySQLdb.connect(
        host='127.0.0.1',
        user='root',
        passwd='123456',
        db='python',
        port=3306,
        charset='utf8'
    )

    # 创建数据库游标,并查询数据
    cursor = conn.cursor()
    cursor.execute(query='select * from news order by create_date asc')
    result = cursor.fetchall()
    print(result)

    # 关闭连接
    cursor.close()
    conn.close()

# 异常处理
except MySQLdb.Error as e:
    # 打印异常
    print('Error: %s' % e)

