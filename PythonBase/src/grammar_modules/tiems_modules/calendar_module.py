# -*- coding: utf-8 -*-
'''
    calendar 日历模块
        创建年,月,周的格式化表示。它还可用于计算经常性事件，给定日期的一周中的某天以及其他基于日历的值
'''

import calendar
import pprint
import sys


if __name__ == '__main__':
    c = calendar.TextCalendar(calendar.SUNDAY)
    c.prmonth(2017, 7)

    cal = calendar.Calendar(calendar.SUNDAY)

    cal_data = cal.yeardays2calendar(2017, 3)
    print('len(cal_data)      :', len(cal_data))

    top_months = cal_data[0]
    print('len(top_months)    :', len(top_months))

    first_month = top_months[0]
    print('len(first_month)   :', len(first_month))

    print('first_month:')
    pprint.pprint(first_month, width=65)

    cal = calendar.TextCalendar(calendar.SUNDAY)
    print(cal.formatyear(2017, 2, 1, 1, 3))

    c = calendar.LocaleTextCalendar(locale='en_US')
    c.prmonth(2017, 7)

    print()

    c = calendar.LocaleTextCalendar(locale='fr_FR')
    c.prmonth(2017, 7)

    year = int(sys.argv[1])

    # Show every month
    for month in range(1, 13):

        # Compute the dates for each week that overlaps the month
        c = calendar.monthcalendar(year, month)
        first_week = c[0]
        second_week = c[1]
        third_week = c[2]

        # If there is a Thursday in the first week,
        # the second Thursday is # in the second week.
        # Otherwise, the second Thursday must be in
        # the third week.
        if first_week[calendar.THURSDAY]:
            meeting_date = second_week[calendar.THURSDAY]
        else:
            meeting_date = third_week[calendar.THURSDAY]

        print('{:>3}: {:>2}'.format(calendar.month_abbr[month],
                                    meeting_date))