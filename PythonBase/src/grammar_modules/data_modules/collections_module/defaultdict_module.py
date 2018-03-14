# -*- coding: utf-8 -*-
'''
    defaultdict
        具有缺省键的字典结构
'''

from collections import defaultdict

# 返回默认值的函数
def default_factory():
    return 'default value'

if __name__ == '__main__':
    # 创建defaultdict对象,传入返回默认值的函数,并将其他的字典元素,通过键值对的形式传入
    d = defaultdict(default_factory, foo='bar')
    # 类型是defaultdict类型,含有一个默认值函数和其他已知的键值对
    print('d:', d)
    # 正常取出已有的值,当不存在时,返回默认值函数中设定好的默认值
    print('foo =>', d['foo'])
    print('bar =>', d['bar'])