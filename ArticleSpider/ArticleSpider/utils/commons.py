# -*- coding: utf-8 -*-

# 各种工具方法

import hashlib

# md5加密算法
def get_md5(string):
    # Python3全部使用UnionCode,这里首先进行转码,随后进行摘要
    if isinstance(string,str):
        string = str.encode('UTF-8')
    md5 = hashlib.md5()
    md5.update(string)
    return md5.hexdigest()
