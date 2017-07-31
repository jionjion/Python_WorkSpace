# 生成一个新的范围内数组.

# 范围输出
arr =  range(1, 11);                    # [1,11)以内的数
print(arr);

# 表达式输出
arr =  [x * x for x in range(1, 11)]    # 表达式  for 变量 in range(开始,结束) if 变量判断表达式
print(arr); 

# 判断后表达式输出
arr = [x * x for x in range(1, 11) if x % 2 == 0]   # if后为变量判断表达式
print(arr);

# 排列组合
arr = [m + n for m in 'ABC' for n in '123'];    # 表达式  for 变量A in 范围    for  变量B  in  范围 
print(arr);

print("")

print ([(i*100)+(j*10)+k for i in range(1,10) for j in range(0,10) for k in range(0,10) if i==k]);