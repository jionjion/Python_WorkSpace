# -*- coding: utf-8 -*-

import re

str_one = "hello world";

print("hello的开始位置:",str_one.find("hello"));
print("是否以hello开始:",str_one.startswith("hello"));
print("是否以hello结束:",str_one.endswith("hello"));

#匹配以world结尾换行的字符串
pa = re.compile(r"^world");                                         #传入语法规则
ma = re.match(str_one,"^world");                                                  #传入进行匹配的字符串
ma.group();

