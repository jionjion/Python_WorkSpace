# -*- coding: utf-8 -*-
'''
    主要的启动方法,便于调试
'''

from scrapy.cmdline import execute
import sys
import os

if __name__ == '__main__':
    # 获得当前运行文件的父文件夹目录,作为
    print('执行项目路径:',os.path.dirname(os.path.abspath(__file__)))
    # 将运行文件的位置,添加到系统执行路径中
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    # 使用命令组合,调用命令行启动程序,执行其中一个爬虫子项目
    execute(['scrapy', 'crawl', 'bai_du_feng_yun'])