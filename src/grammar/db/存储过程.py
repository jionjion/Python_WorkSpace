import pymysql                                  #导入模块,记得将模块放入library下编译

# 获得pymysql的安装位置
# print(pymysql);

# 获取数据库连接
conn = pymysql.Connect(host="127.0.0.1", user="root", password="123456",
                 database="python", port=3306,charset='utf8');

# 获得数据库游标,默认抓取的数据结构为元组类型
cursor = conn.cursor();
try:
    # 调用
    """
                    这里写存储过程
    """
    
    # 事务提交
    conn.commit();
except Exception as e:                                  #如果出现异常,则回滚
    print("事务执行出现异常:",e);
    # 事务回滚
    conn.rollback();

finally:
    # 关闭游标
    cursor.close();
    
    # 关闭连接
    conn.close();












