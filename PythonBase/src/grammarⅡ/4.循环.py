# -*- coding: utf-8 -*-

循环
while 循环
最为递归,或者条件判断

while 条件 :
    代码块
else:
    无论如何下,都情况下的代码块(可选)


for 循环
主要用来遍历/循环 序列,集合,字典

for 对象  in  序列/集合/字典 :
    代码块
else:
    无论如何都会执行的代码块(可选)


break 强制结束,不会执行else的代码块,多层次嵌套时,只会跳出第一层循环
continue  跳过

循环,生成[0,10)的数,间隔为2
for x in range(0,10,2):
    print(x,end=' | ')

print()

