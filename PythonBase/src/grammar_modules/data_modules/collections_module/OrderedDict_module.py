# -*- coding: utf-8 -*-
'''
    OrderedDict
        具有顺序的字典元素
'''
from collections import OrderedDict

if __name__ == '__main__':
    # 创建OrderedDict有序字典对象,字典的存入顺序就是遍历属性.
    # 注意,两个不同的顺序创建的相同内容的OrderedDict被看做不同的类型
    d = OrderedDict()
    d['a'] = 'A'
    d['b'] = 'B'
    d['c'] = 'C'

    # 遍历与输出
    for k, v in d.items():
        print(k, v)

    # 将其中一个元素移动到开头
    d.move_to_end('b', last=False)
    # 将其中一个元素移动到结尾
    d.move_to_end('b', last=True)
    print(d)

