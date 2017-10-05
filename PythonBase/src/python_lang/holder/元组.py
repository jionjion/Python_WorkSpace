
# 创建元组
empty_tuple = ();

# 创建单元素元组
single_tuple = ('hello',);

# 创建多元素元组
many_tuple = ('星期一 ','星期二','星期三');

# 元组解包
monday,tuesday,wednesday = many_tuple;

# 通过list列表创建元组
many_list = ('星期四','星期五','星期六');
many_tuple= tuple(many_list); 

print(monday);