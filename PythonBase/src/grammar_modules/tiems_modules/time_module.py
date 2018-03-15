# -*- coding: utf-8 -*-
'''
    Time模块
        公开了底层C库中与时间相关的功能,比较基础
        它包括用于检索时钟时间和处理器运行时间的函数，以及基本的分析和字符串格式化工具。
'''

import time
if __name__ == '__main__':

    # 获得当前秒数,可以根据操作系统认为设定系统时间 1970年1月1日0时
    print(time.time())
    # 格式化,可以传入时间秒数,获得当时时间
    print(time.ctime(time.time() + 30))

    # 获得当前系统开机持续时间 单位秒
    print(time.monotonic())

    # 处理器时钟,反应程序执行时间,不会随线程休眠而时间增长
    print(time.clock())

    # 执行计时 [perf_counter] 函数用来计算高精度的一段时间
    print(time.perf_counter() - time.perf_counter())


    # 日期组件,获得日期的 年 月 日 时 分 秒

    # 获得 UTC 世界标准时间
    print(time.gmtime())
    # 获得当前时区时间
    print(time.localtime())
    # 当地时区信息
    print('年:', time.localtime().tm_year)
    print('月:', time.localtime().tm_mon)
    print('日:', time.localtime().tm_mday)
    print('时:', time.localtime().tm_hour)
    print('分:', time.localtime().tm_min)
    print('秒:', time.localtime().tm_sec)
    print('星期:', time.localtime().tm_wday)      # [0, 6], Monday is 0
    print('一年中天数:', time.localtime().tm_yday)

    # 字符串转为日期
    print(time.strptime('2018-1-1','%Y-%m-%d'))
    # 日期转为字符串,默认转换当前时间
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.strptime(time.ctime())))