# -*- coding: utf-8 -*-

'''
    enum 枚举模块
'''
import enum

# 定义枚举类,继承Enum类
class Weekend(enum.Enum):
    # 键值对
    Mon = 'Monday'
    Tue = 'Tuesday'
    Wed = 'Wednesday'
    Thu = 'Thursday'
    Fri = 'Friday'
    Sat = 'Saturday'
    Sun = 'Sunday'
    Sab = 'Sunday'          # 相同的值,其枚举名会被看做是之前首次出现的枚举名的别名,并别不会被迭代出


if __name__ == '__main__':
    # 枚举名
    Weekend.Mon.name
    # 枚举值
    Weekend.Mon.value

    # 迭代枚举
    for w in Weekend:
        print('name:',w.name,'   value:',w.value)

    #