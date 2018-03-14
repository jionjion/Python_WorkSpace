# -*- coding: utf-8 -*-
'''
    ChainMap — 可以搜索的字典类型
'''
from collections import ChainMap

if __name__ == '__main__':
    # 创建字典
    a = {'Mon': 'Monday', 'Tue': 'Tuesday','Wed':'Wednesday'}
    b = {'Wed':'wednesday','Thu': 'Thursday', 'Fri': 'Friday','Sat':'Saturday'}
    c = {'Sun':'Sunday'}

    # 将多个字典聚合,构成一个字典
    week = ChainMap( a , b)
    # 无论修改原来的字典或者后来的字典,值均会发生改变
    week['Mon'] = 'monday'
    a['Tue'] = 'tuesday'
    # 当键名相同时,只会修改匹配的第一个元素
    week['Wed'] = 'wednesday!'

    # 类型为ChainMap类型
    print(week)
    # [.maps] 函数,将内部的转为字典列表.reversed函数,可以反转列表
    print(week.maps)
    print('Keys = {}'.format(list(week.keys())))
    print('Values = {}'.format(list(week.values())))

    # 使用 [,items()] 方法,迭代
    for k, v in week.items():
        print('{} = {}'.format(k, v))
    print()

    # in 判断是否在里面
    print('"Sun"是否在字典中: {}'.format(('Sun' in week)))
