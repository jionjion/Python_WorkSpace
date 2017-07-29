# set集合
# 无序,且不重复
# 作用:常判断输入元素是否合法
user = set(['Arise', 'Tom', 'Jion']);               #传入数组为set集合

print('Bart' in user);                              #判断元素是否在当前set集合中
 
print(user);                                        #直接输出set集合

for u in user:                                       #遍历set集合r
    print(u);                                       #输出

user.add("Zoo");                                    #增加一个元素,如果存在则不会增加

if "Zoo" in user:                                   #首先判断是否存在,再删除
    user.remove("Zoo");                             #如果直接删除不存在元素.会抛出异常
