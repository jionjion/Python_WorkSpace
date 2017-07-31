# 通过索引迭代,读取集合的索引以及元素

userList = ['Adam', 'Lisa', 'Bart', 'Paul'];
for index,value in enumerate(userList):
    print("索引:",index,"值:",value);
    
    
    
# 通过迭代,完成dict数据结构的遍历
score = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 };
for key, value in score.items():
    print("键:",key,"值:",value);