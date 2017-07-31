# 使用dict类型,完成key-value键值对的储存

score = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
};

score['Lisa'] = 72;                     #如果key名称相同,则为更新键,否则为插入键值对

if 'Bart' in score:                     #使用if..in..进行判断,然后取出key对应的值
    print(score['Bart']);               #如果直接取值,如果值为不存在,则会抛出异常
    
print(score.get('Bart'));               #使用get()方法,获取值,如果没有,则会返回空,避免异常

for key in score:
    print(key,score.get(key));          #通过迭代key获取value

print("长度",len(score));                 #获取dict的长度