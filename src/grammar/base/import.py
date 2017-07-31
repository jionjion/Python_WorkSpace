# 导入包
import math;                                        #导入
from math import pow, sin, log;                     #导入包下的具体函数
from math import pow as pw;                         #导入函数后起别名

# 动态导入包
try:
    from cStringIO import StringIO                  #尝试导入这个包,如不存在,则抛出异常
except ImportError:                                 #如果抛出异常,则导入这个包,完成动态导入包
    from StringIO import StringIO
    
