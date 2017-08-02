# -*- coding: utf-8 -*-

#以hello开头的文本,将其打印出
def find_start_with_hello(file_name):
    file = open(file=file_name, mode="r", encoding="UTF8");
    for line in file:
        if line.startswith('hello'):                                        #.startswith()以XX开头的
            print(line);
        
#以hello开头和结尾的文本,将其打印出
def find_start_with_hello_and_end_with_hello(file_name):
    file = open(file=file_name, mode="r", encoding="UTF8");
    for line in file:
        if line.startswith('hello') and line.endswith('hello'):             #.endswith()以XX结尾
            print(line);

#调用,hello开头的
find_start_with_hello("file_one");

#调用,hello开头结尾的
find_start_with_hello_and_end_with_hello('file_one');        