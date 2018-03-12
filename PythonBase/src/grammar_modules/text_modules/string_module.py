# -*- coding: utf-8 -*-
'''
    string模块
        许多功能已经被移到了str对象的方法中
'''

import string

if __name__ == '__main__':

    hello = "hello everybody , I'am Jion! "

    ''' 
        capwords
            首字符大写
    '''
    print(string.capwords(hello))
