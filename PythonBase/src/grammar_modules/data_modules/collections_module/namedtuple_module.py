# -*- coding: utf-8 -*-
'''
    namedtuple  具有字段名的元组类型
        可以看做为具有域的散列,简化对象

'''
from collections import namedtuple
if __name__ == '__main__':

    # 定义一种元组类型,指定类型名和其字段名,字段名不可以修改
    People = namedtuple(typename='People',field_names=['name','age'])
    # 为元组赋值
    jion = People(name='Jion' , age = 23)
    # 使用 .字段 获得对象的值
    print(jion.name)
    # 使用 *获得对象的所有属性值
    print(*jion)