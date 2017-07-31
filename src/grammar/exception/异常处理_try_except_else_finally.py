# 使用  try..except..else..finally方式处理异常
# 

try:                                #尝试执行语句
    print(1/1);
except ZeroDivisionError as e:      #捕获零除异常
    print("零除异常",e)   
except Exception as e:              #捕获其他异常
    print("其他异常",e)
else:                               #如果没有异常出现,则会继续执行该语句块
    print("如果没有异常,则继续执行")          
finally:                            #一定会执行,如果有异常抛出,则在异常处理代码块前执行
    print("执行其他清理任务");    