
# 定义函数
def commentary(color,other = "其他颜色"):     # 接受任何数量（包括 0）的任何类型的值作为输入变量
    if color == 'red':                                    
        return "这是红色"                     # 任何数量（包括 0）的任何类型的结果              
    elif color == "green":
        return "这是绿色"
    elif color == 'purple':
        return "这是紫色"   
    else:
        return "没有见过" + other + "."       # 不声明时,默认返回 None

# 调用函数




# 位置参数,如上所示,每一个传入的参数位置需要固定,不能交换位置
context = commentary('red');
# 关键字参数,使用=进行关键字赋值
context = commentary(color="blue");
# 默认参数,在形参中添加=赋值默认值,注意:当默认值为容器时,会在每次调用时往容器中装入新值


# *代表参数为元组类型,支持传入多个参数,多用来放在参数列表最后,以便收集多余变量
def print_args(*args):
    print(args);

print_args(1,2,3,4,5,6);

# **代表关键词字典,传入关键词参数形式,进行字典赋值
def print_kwargs(**kwargs):
    print('Keyword arguments:', kwargs)

print_kwargs(monday='星期一',tuesday='星期二',wednesday='星期三');

# 文档字符串
def print_help():
    '这是一个帮助文档...哔哩哔哩..,使用help(函数名)调用'

print(print_help.__doc__);          # 查看帮助文档信息  


# 内部函数
def knights(saying):
    # 在函数内部声明自定义函数
    def inner(quote):
        return "We are the knights who say: '%s'" % quote;
    # 执行自定义函数,并将结果返回
    return inner(saying);

# 闭包..

# 匿名函数,通过在参数列表中,传入函数对象,再由参数函数对象调用方法,完匿名函数的调用
