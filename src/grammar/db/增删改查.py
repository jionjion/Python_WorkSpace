import pymysql                                  # 导入模块,记得将模块放入library下编译

# 获得pymysql的安装位置
# print(pymysql);

# 获取数据库连接
conn = pymysql.Connect(host="127.0.0.1", user="root", password="123456",
                 database="python", port=3306,charset='utf8')

# 获得数据库游标
cursor = conn.cursor();

print(cursor);

# 执行sql,将查询结果存入客户端的本地缓冲区
sql_select = "select * from user";
cursor.execute(sql_select);

# 打印查询的记录数量
print("查询记录数:",cursor.rowcount);

# 抓取一条记录
rs = cursor.fetchone();
print("抓取一条记录:",rs);

# 抓取指定记录
rs = cursor.fetchmany(2);
print("抓取两条记录",rs);

# 抓取全部记录
rs = cursor.fetchall();
print("抓取剩余记录",rs);

# 对抓取的数据进行解析
for row in rs:
    print("用户名:",row[1])

# 事务开启,默认自动提交事务是关闭的.如果不执行commit操作,数据的增删改是不会发生改变的
try:
    
    # 增加记录
    sql_insert = "insert into user(id,username) values(6,'Jam')";
    cursor.execute(sql_insert);
    # 修改记录
    sql_update = "update user set username = 'Jaker' where id = 6";
    cursor.execute(sql_update);
    # 删除记录
    sql_delete = "delete from user where id = 3 "
    cursor.execute(sql_delete);
    print("影响的记录数",cursor.rowcount);
    # 事务提交
    conn.commit();
except Exception as e:
    print("事务执行出现异常:",e);
    # 事务回滚
    conn.rollback();

# 关闭游标
cursor.close();

# 关闭连接
conn.close();












