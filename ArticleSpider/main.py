# -*- coding: utf-8 -*-
'''
    项目入口函数
    便于调节
'''
from scrapy.cmdline import execute
import sys
import os

if __name__ == '__main__':
    # 获得当前运行文件的父文件夹目录,作为
    print('执行项目路径:',os.path.dirname(os.path.abspath(__file__)))
    # 将运行文件的位置,添加到系统执行路径中
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    execute(['scrapy', 'crawl', 'jobbole'])