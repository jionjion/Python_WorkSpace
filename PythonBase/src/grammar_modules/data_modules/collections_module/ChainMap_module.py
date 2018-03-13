# -*- coding: utf-8 -*-
'''
    ChainMap — 可以搜索的字典类型
'''
from collections import ChainMap

if __name__ == '__main__':
    # 创建字典
    a = {'a': 'A', 'c': 'C'}
    b = {'b': 'B', 'c': 'D'}

    # 将多个字典聚合,构成一个字典
    m = ChainMap( a , b)

    print('Individual Values')
    print('a = {}'.format(m['a']))
    print('b = {}'.format(m['b']))
    print('c = {}'.format(m['c']))
    print()

    print('Keys = {}'.format(list(m.keys())))
    print('Values = {}'.format(list(m.values())))
    print()

    print('Items:')
    for k, v in m.items():
        print('{} = {}'.format(k, v))
    print()

    print('"d" in m: {}'.format(('d' in m)))