# 使用with语句完成异常捕获,但是不进行异常的处理
#
#     with context [as var]:
#        with_suite
#
# context表达式返回的是一个对象
# var用来保存返回对象,单个返回值或者元组
# with_suite 使用var变量来对context返回对象进行操作

with open("文件.txt") as f:
    print("读取内容:",f.read());

print("文件状态:",f.closed);


# 上下文管理协议:包含__enter__()和__exit__()方法,支持该协议的对象要实现这两个方法
# 
# 上下文管理器:定义执行with语句时要建立在运行时上下文,负责执行with语句块的进入与退出操作
# 
# 进入上下文管理器:调用管理器的__enter__方法,如果设置as var语句,var变量接收__enter__()方法的返回值
# 
# 退出上下文管理器:调用管理器__exit__方法