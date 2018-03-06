# -*- coding: utf-8 -*-

匿名函数    在定义函数的时候,不需要指定函数名

def add( x , y ):
    return  x + y

# 匿名函数 lamdba 参数列表 : 函数主体
lambda x , y : x + y

# 三元表达式,求最大值
条件真的返回结果  if 条件判断  else 条件为假的返回结果
x if x > y else y


map 类实现批量计算
list_x = [1,2,3,4,6]
def square(x):
    return  x * x
# 求每个数的平方
for x in list_x:
    square(x)
# 使用map对传入序列的每一项根据表达式进行计算
result = map(square,list_x)
# 使用lambda表达式进行替换,x代指map中传入的列表每一个变量
result = map(lambda x : x*x,list_x)
print(list(result))

例如:列表长度不同时,返回结果以最短列表为主
list_x = [1,2,3,4]
list_y = [4,5,6,7]
result = map(lambda x , y : x + y , list_x , list_y)
print(list(result))


reduce函数,进行连续累计计算, 求和,上一次执行结果迭代 1 + 2 + 3 +4
from functools import reduce
list_x = [1,2,3,4]
result = reduce(lambda x , y : x + y , list_x , 10) # 10 可选参数,表示y在第一次运算时的参与的值
print(result)

filter函数,表达式返回布尔值,当为True时,保留;False时,过滤
list_x = [1,1,0,1,0,1,0]
result = filter(lambda x:True if x==1 else False , list_x)
print(list(result))
