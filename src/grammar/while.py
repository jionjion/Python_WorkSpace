# while循环
i = 0;
while i<5:
    print("循环继续...");
    i=i+1;
    
    
i = 0;
while i<=10:
    print("break打断继续...");
    break;                              #使用break强制结束
    i=i+1;    
    
tol = 0;                                #计算10以内的奇数和
x = 0;
while True:                             #表示无条件执行
    x = x + 1;
    if x > 10:                          #逻辑判断
        break;                          #如果大于10,则跳出循环
    if x%2==0:                          #求余为0,为偶数,跳过
        continue;                       #跳过
    tol = tol + x;
print(tol);    

