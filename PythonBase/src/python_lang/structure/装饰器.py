# 不改变源代码的情况下修改已经存在的函数。
# 装饰器实质上是一个函数。 它把一个函数作为输入并且返回另外一个函数。
# 技巧:*arg 和 **kwargs    闭包        作为参数的函数

# 第一种创建装饰器的方式..
# 定义装饰器
def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function;

# 自定义原来的函数,求和,使用代码动态编译
def add_int_by_code(a,b):
    return  a+b;

# 使用装饰器
new_add_int = document_it(add_int_by_code);
new_add_int(5,3);


# 第二种创建装饰器的方式
# 定义装饰器不变..

# 自定义原来的函数,求和

# 使用注解,注解为装饰器的名字,修改原函数.
# 可以注解多个,完成装饰器的轮流使用
@document_it
def add_int_by_annotate(a,b):
    return  a+b;
# 使用装饰器
add_int_by_annotate(4,6);