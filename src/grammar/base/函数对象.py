# 函数的练习
from _functools import reduce
import math                                     #导入math


# 使用极坐标公式,计算偏移量
def move(x, y, step, angle):                    #def关键字,定义函数
    nx = x + step * math.cos(angle)             #同一个缩进中,完成代码块的编写
    ny = y - step * math.sin(angle)             #极坐标公式
    return nx, ny;                              #return关键字,返回函数结果,可以为单个参数,也可以为多个参数包装的tuple结构

x,y=move(10, 10, 50, 45);
print(x,y);

# 使用递归函数,完成阶乘函数
def factorial(x):
    if x==1:                                    #第二步,定义结束条件,使用return返回结果
        return 1;
    return x*factorial(x-1);                    #修改递归变量,传入函数名,修改变量
x=factorial(3);
print("3的阶乘为:",x);

# 具有默认参数的函数,求一个数的次方,没有传入则表示求平方
def power(x, n=2):
    s = 1;
    while n > 0:
        n = n - 1
        s = s * x                               #自乘了n次
    return s
print("默认2的次方?:",power(2));
print("2的3次方:",power(2,3));

# 参数可变的函数
def fn(*args):
    print(args)

fn("哔哩哔哩","Jion");

# 将函数作为参数传入
def add_abs(x, y, f):                               #求两个数的绝对值的和
    return f(x) + f(y);
print('两个数的绝对值和:',add_abs(2, -2, abs));          #将函数名作为参数传入

# map,函数映射,按照既定规则,完成映射.
def map_fn(x):                                      #将传入数组元素的x平方后传入新数组
    return  x*x;                                    #返回结果

oldNumList = [1,2,3,4,5,6];
newNumList = map(map_fn,oldNumList);                #将函数句柄传入,传入转换前的list,完成转出
print("转换后:",list(newNumList));                    #使用lsit的构造函数,完成map结果的list转化输出

# reduce,函数自映射,将list每个进行操作,计算结果为一个数字
def reduce_fn(x,y):                                 #传入list中的元素,x代表第一个或者计算结果,y代表list的下一个
    return x+y;                                     #对list中的作求和运算
oldNumList = [1,2,3,4,5]
newNumList = reduce(reduce_fn, oldNumList, 100);    #计算结果为一个数字
print("转换后:",newNumList);

# filter,据判断结果自动过滤掉不符合条件的元素，返回由符合条件元素组成的新list
def filter_fn(x):                                   #自定义过滤函数,根据条件,返回的一个布尔值
    return x % 2 == 1;                              #返回的一个是布尔值,如果是奇数,则返回true,执行过滤,放出
oldNumList = [1,2,3,4,5,6];
print("判断是否为奇数:",list(filter(filter_fn,oldNumList)));
# filter,过滤空串
def filter_empty_fn(s):
    return s and len(s.strip()) > 0                  #s不为空则默认为true,同时,s裁剪后长度大于?0,则最终返回true.作为过滤条件
print("过滤空串后:",list(filter(filter_empty_fn,['test', None, '', 'st', '  ', 'END'])));

# sorted,自定义排序.传入两个待比较的元素 x, y，如�? x 应该排在 y 的前面，返回 -1，如�? x 应该排在 y 的后面，返回 1。如果x和y相等，返0
# 返回-1,为位置不变;返回1,位置交换;返回0,位置不变
# def reversed_fn(x, y):                              #自定义排序,降序排列
#     if x > y:                                       #由大到小,不改变位置  
#         return -1
#     if x < y:                                       #有小到大,改变位置
#         return 1
#     return 0                                        #默认不改变
# oldNumList = [1,2,3,4,5];
# newNumList = sorted(oldNumList,reversed_fn);
# print("降序排列后:",newNumList);                       
#