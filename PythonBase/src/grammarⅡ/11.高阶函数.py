# -*- coding: utf-8 -*-

# 闭包 = 函数定义 + 函数变量
# 闭包,函数和其环境变量构成的一个整体,当其构成闭包时,环境变量不会受其他变量的影响

# 外部函数
def curve_pre():
    # 定义内部值,当未定义时,将寻找上级的环境变量
    a = 25
    # 内部函数
    def curve(x):
        print('内部函数!')
        # 当a引用外部a的时候,构成闭包
        return a*x*x
    # 将内部函数结果
    return curve

# 调用外部函数,返回内部函数给一个变量
f = curve_pre()
# 执行返回函数
print(f(2))

# 查看闭包的信息
print(f.__closure__)
# 定义是的环境变量
print(f.__closure__[0].cell_contents)


例一:累计计算,非闭包的方式

tol = 0
def tol_go(step):
    # 声明全局变量
    global tol
    tol = tol + step
    return  tol

# 计算
print( go(10))
print( go(10))
print( go(10))

例二:累计计算,闭包的方式
def tol_go(tol):
    def go(step):
        # 声明不是局部变量
        nonlocal tol
        tol = tol + step
        return tol
    return  go

f = tol_go(0)
print(f(10))
print(f(10))
print(f(10))

