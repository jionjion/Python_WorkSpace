# -*- coding: utf-8 -*-
'''
    datetime    日期模块
        为日期，时间和组合值提供更高级别的界面。在类datetime支持算术，比较，和时区的配置。
        符号	含义	                                例
        %a	缩写周日名称	                       'Wed'
        %A	完整的周日名称	                        'Wednesday'
        %w	星期 - 0（星期日）至6（星期六）	        '3'
        %d	本月日（零填充）	                    '13'
        %b	缩写的月份名称	                        'Jan'
        %B	全月名称	                            'January'
        %m	一年的月份	                            '01'
        %y	没有世纪的一年	                        '16'
        %Y	有世纪的一年	                        '2016'
        %H	小时从24小时制	                        '17'
        %I	小时从12小时制	                        '05'
        %p	上午下午	                            'PM'
        %M	分钟	                                '00'
        %S	秒	                                    '00'
        %f	微秒	                                '000000'
        %z	时区对UTC的偏移量	                    '-0500'
        %Z	时区名称	                            'EST'
        %j	一年中的一天	                        '013'
        %W	一年中的一周	                        '02'
        %c	当前语言环境的日期和时间表示	        'Wed Jan 13 17:00:00 2016'
        %x	当前语言环境的日期表示	                '01/13/16'
        %X	当前语言环境的时间表示	                '17:00:00'
'''

import datetime

if __name__ == '__main__':

    # 时间 , 可以传入时分秒,默认00:00:00
    time = datetime.time(hour=8, minute=30, second=15, microsecond=125000)
    # 获得时间的时分秒,需要先实例化time对象
    print(time.hour, time.minute, time.second)
    # 时间最大值
    print(time.max)
    # 时间最小值
    print(time.min)
    # 时间精度
    print(time.resolution)

    # 日期
    today = datetime.date.today()
    print('今天:', today)
    print('年:', today.year)
    print('月:', today.month)
    print('日:', today.day)
    print('日:', today.toordinal())
    print('日期对象', today.ctime())

    # 转为时间元组
    tt = datetime.date(year=2018, month=1, day=1).timetuple()
    print('年:', tt.tm_year)
    print('月:', tt.tm_mon)
    print('日:', tt.tm_mday)
    print('时:', tt.tm_hour)
    print('分:', tt.tm_min)
    print('秒:', tt.tm_sec)
    print('本周天', tt.tm_wday)    # 0表示周期一
    print('本年月', tt.tm_yday)
    print('是否含有夏令时', tt.tm_isdst)

    # 日期设定  [timedelta] 作为日期计算对象
    print('microseconds:', datetime.timedelta(microseconds=1))
    print('milliseconds:', datetime.timedelta(milliseconds=1))
    print('seconds     :', datetime.timedelta(seconds=1))
    print('minutes     :', datetime.timedelta(minutes=1))
    print('hours       :', datetime.timedelta(hours=1))
    print('days        :', datetime.timedelta(days=1))
    print('weeks       :', datetime.timedelta(weeks=1))

    # 日期计算
    today = datetime.date.today()
    print('Today    :', today)

    one_day = datetime.timedelta(days=1)
    print('One day  :', one_day)

    yesterday = today - one_day
    print('Yesterday:', yesterday)

    tomorrow = today + one_day
    print('Tomorrow :', tomorrow)

    print('tomorrow - yesterday:', tomorrow - yesterday)
    print('yesterday - tomorrow:', yesterday - tomorrow)

    one_day = datetime.timedelta(days=1)
    print('1 day    :', one_day)
    print('5 days   :', one_day * 5)
    print('1.5 days :', one_day * 1.5)
    print('1/4 day  :', one_day / 4)

    # 比较日期
    print('Times:')
    t1 = datetime.time(12, 55, 0)
    print('  t1:', t1)
    t2 = datetime.time(13, 5, 0)
    print('  t2:', t2)
    print('  t1 < t2:', t1 < t2)

    print('Dates:')
    d1 = datetime.date.today()
    print('  d1:', d1)
    d2 = datetime.date.today() + datetime.timedelta(days=1)
    print('  d2:', d2)
    print('  d1 > d2:', d1 > d2)

    # 结合日期时间
    print('Now    :', datetime.datetime.now())
    print('Today  :', datetime.datetime.today())
    print('UTC Now:', datetime.datetime.utcnow())
    print()

    FIELDS = [
        'year', 'month', 'day',
        'hour', 'minute', 'second',
        'microsecond',
    ]

    d = datetime.datetime.now()
    for attr in FIELDS:
        print('{:15}: {}'.format(attr, getattr(d, attr)))

    t = datetime.time(1, 2, 3)
    print('t :', t)

    d = datetime.date.today()
    print('d :', d)

    dt = datetime.datetime.combine(d, t)
    print('dt:', dt)

    # 日期格式化,解析
    format = "%a %b %d %H:%M:%S %Y"

    today = datetime.datetime.today()
    print('ISO     :', today)

    s = today.strftime(format)
    print('strftime:', s)
    today = datetime.datetime.today()
    print('ISO     :', today)
    print('format(): {:%a %b %d %H:%M:%S %Y}'.format(today))

    d = datetime.datetime.strptime(s, format)
    print('strptime:', d.strftime(format))

    # 时区
    min6 = datetime.timezone(datetime.timedelta(hours=-6))
    plus6 = datetime.timezone(datetime.timedelta(hours=6))
    d = datetime.datetime.now(min6)

    print(min6, ':', d)
    print(datetime.timezone.utc, ':',
          d.astimezone(datetime.timezone.utc))
    print(plus6, ':', d.astimezone(plus6))

    # 转为当前时区
    d_system = d.astimezone()
    print(d_system.tzinfo, '      :', d_system)