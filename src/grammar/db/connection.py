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
sql = "select * from user";
cursor.execute(sql);

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
    print("用户名:",row.get("username"))

# 关闭游标
cursor.close();

# 关闭连接
conn.close();












