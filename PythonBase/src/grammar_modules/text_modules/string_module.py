# -*- coding: utf-8 -*-
'''
    string模块
        许多功能已经被移到了str对象的方法中
'''

import string

if __name__ == '__main__':

    hello = "hello everybody , I'am Jion! "

    # [capwords]    首字符大写
    print(string.capwords(hello))

    # [templates]   模板方法
    temp = string.Template("hello $name , nice to meet you!")   # 创建模板
    # [.substitute] 传入字典,为模板赋值
    print(temp.substitute({'name':'Airse'}))

    # [.format] 占位符,为字符串中{}中的字符进行赋值
    print('hello , {}'.format('world'))

    # %s 占位符,通过%连接一个元组,进行模板赋值
    print('hello , %s'  % ('world',))