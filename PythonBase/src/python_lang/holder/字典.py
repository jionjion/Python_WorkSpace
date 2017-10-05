# 创建空字典
empty_dict = {}


# dict()将双字符串列表转为字典
double_str_list = ['ab','cd','ef'];
double_str_dict = dict(double_str_list);

# dict()将双字符串元组转为字典
double_str_list = ('ab','cd','ef');
double_str_dict = dict(double_str_list);

# dict()将双值子列表转为字典
week_list = [['monday','星期一'],['tuesday','星期二'],['wednesday','星期三']];
week_dict = dict(week_list);

# dict()将双值子元组转为字典
week_tuple = (['monday','星期一'],['tuesday','星期二'],['wednesday','星期三']);
week_dict = dict(week_tuple);


# 使用key添加/修改元素
week_dict['thursday'] = '星期四';

# 删除元素
del week_dict['thursday'];

# in()判断是否存在,返回布尔值
is_exist = 'monday' in week_dict;

# get()获得值或者默认值,存在则返回;不存在,当指定默认值时返回默认值,否则返回None
thursday = week_dict.get('thursday','星期四');

# keys()获得所有键的列表,为dict_keys键的元组迭代形式,需要手动转为转为列表
dict_keys = week_dict.keys();
keys_list = list(dict_keys);

# values()获取所有值,返回dict_values值的元组迭代形式,需要手动转为转为列表
dict_values = week_dict.values();
values_list = list(dict_values);

# items()获得所有键值对,返回dict_items键值对的元组迭代形式,需要手动转为列表
dict_items = week_dict.items();
items_list = list(dict_items);

# copy(),复制一个字典
week_dict_copy = week_dict.copy();

# 使用update()方法将元素合并,新的值会修改旧的值
week_dict.update(double_str_dict);

# 清空字典
week_dict.clear();