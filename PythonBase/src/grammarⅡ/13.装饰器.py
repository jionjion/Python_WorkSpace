# -*- coding: utf-8 -*-

import time

# 装饰器,传入要执行的函数,在其前后新增方法,打印时间
def decorator(func):
    # 包装函数,参数列表为可变参数列表和关键词参数
    def wrapper(*args , **kwargs):
        print(time.time())
        print('Now time!')
        func(*args , **kwargs)
    return wrapper


@decorator
def fn1(param):
    print('others....' , param)

@decorator
def fn2(param1 , param2):
    print('others....' , param1 , param2)

@decorator
def fn3(param1, param2 , **kwargs):
    print('others....' , param1 , param2 , kwargs)
# # 调用装饰器
# f = decorator(fn);
# f()

# 单参数的函数调用装饰器
fn1('A')
# 多参数的函数调用调用装饰器
fn2('A','B')
# 多参数,关键词参数函数调用装饰器
fn3('A','B',C=1)