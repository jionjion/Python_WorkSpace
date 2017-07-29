'''
    列表数组的练习,注意缩进以及换行
''';

userList = ['Jion','Aries'];
#打印全部元素
print(userList);
#打印第一个元素,默认从0开始脚标
print(userList[0]);
#打印倒数第一个元素,索引为负数,表示从后往前进行索引
print(userList[-1]);
#追加一个元素
userList.append("Tom");
#插入一个元素
userList.insert(0, "Angler");
#更新元素
userList[0] = 'Admin';
#删除最后一个元素,并返回该元素
userList.pop();
#删除指定位置的元素
userList.pop(1);


#创建元组,不可变的数组列表类型
userList = ('Jion','Aries');
#打印全部元素
print(userList);
#打印第一个元素,默认从0开始脚标
print(userList[0]);
#打印倒数第一个元素,索引为负数,表示从后往前进行索引
print(userList[-1]);

#单元素的元组,需要在其后加,表示只有一个.
user = ('Jion',)
print(user);

