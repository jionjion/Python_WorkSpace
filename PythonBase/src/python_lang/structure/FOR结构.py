# for循环经常作为各种集合的遍历方式,在长度未知的情况下完成遍历过程

# 迭代列表
week = ['星期一 ','星期二','星期三'];
for itme in week:
    print(itme);

# 迭代元组
week = ('星期一 ','星期二','星期三');
for itme in week:
    print(itme);

# 迭代字符串,拆分为单个字符
word = "word";
for k in word:
    print(k);
    
# 迭代字典
week = {'monday':'星期一','tuesday':'星期二','wednesday':'星期三'};
for key in week.keys():
    print(key);
    
for value in week.values():
    print(value);

# for...else,用来执行else中定义的过程
for i in []:
    print(i);
else:
    print("程序结束");
    
# zip()并行迭代相同维度的数组,经过zip()压缩后为一个多元素的元组的序列
week_en = ['monday','tuesday','wednesday'];
week_cn = ['星期一','星期二','星期三'];
for i,j in zip(week_cn,week_en):
    print(i,j);

# range()生成整数序列,指定初始值,结束值,步长(可以为负,表示反向,注意初始值和结束值的大小关系)
for i in range(0,10,2):         #小于10内的偶数
    print(i);

for i in range(0,-10,-2):       #大于-10内的偶数
    print(i);
