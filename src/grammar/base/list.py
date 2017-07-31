# list有序列表练习

userList = ['Jion','Aries',"Hiz","Ezir"];
#打印全部元素
print("全部元素:",userList);
#打印第一个元素,默认下角从0开始
print("第一个:",userList[0]);
#打印倒数第一个元素,索引为负数,表示从后往前进行索引
print("倒数第一个:",userList[-1]);
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

# list切片,截取任意长度的集合,返回一个新的list,不会修改原数据结构
# 参数  >> 初始位置(缺省表示开始):结束位置(缺省表示结束):每几个分组(缺省表示一个一组)
print("切片后:",userList);
# 截取前两个元素
users = userList[0:2];
users = userList[:2];
# 截取后两个元素
users = userList[-2:];


# 截取全部
users = userList[:];
# 从开始到结束,每两个取一个
users = userList[::2];


print("切片:",users);


users = userList[-2:];
# 倒叙切片


print("前三个:",userList);

#创建元组,不可变的数组列表类型
userList = ('Jion','Aries');
#打印全部元素
print("全部元素:",userList);
#打印第一个元素,默认下角标从0开始
print("第一个元素:",userList[0]);
#打印倒数第一个元素,索引为负数,表示从后往前进行索引
print("倒数第一个:",userList[-1]);

#单元素的元组,逗号要在其后,表示只有一个
user = ('Jion',)
print("唯一元素:",user);



