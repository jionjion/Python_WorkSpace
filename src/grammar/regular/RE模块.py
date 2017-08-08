# -*- coding: utf-8 -*-

import re

str_one = "hello world";

print("hello的开始位置:",str_one.find("hello"));
print("是否以hello开始:",str_one.startswith("hello"));
print("是否以hello结束:",str_one.endswith("hello"));

# re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
# pattern:正则字符规则    string:匹配的字符串    flags:匹配模式
# re.match(pattern, string, flags=0)
        
#匹配以hello开头的字符串
ma = re.match("hello",str_one);                                                  #传入进行匹配的字符串

# group(num=0):返回匹配的结果
# groups():返回匹配的结果们
print(ma.group());

# search:扫描整个字符串并返回第一个成功的匹配。
# pattern:正则字符规则    string:匹配的字符串    flags:匹配模式
# re.search(pattern, string, flags=0)

# 查找是否有hello的字符串
ma = re.search("hello",str_one);                                                
print(ma.group(0));

# re.sub用于替换字符串中的匹配项
# pattern:正则字符规则     repl:替换的字符串，也可为一个函数    string:要被查找替换的原始字符串。    count: 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
# re.sub(pattern, repl, string, count=0, flags=0)

# 查找电话号码
phone = "2004-959-559 # 这是一个电话号码";          
num = re.sub(r'\D', "", phone);                                                 #删除非数字(-)的字符串
print("电话号为:",num)


# 将匹配的数字乘于 2
def sub_fn(matched):                                                            #定义函数
    value = int(matched.group('value'))                                         #匹配值,并类型转换
    return str(value * 2)                                                       #返回计算值,类型转换
 
s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', sub_fn, s));                                     #匹配数组