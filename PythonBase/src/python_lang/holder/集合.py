# 创建一个空集合
empty_set = set();

# 创建集合
even_set = {0,2,4,6,8};
odd_set = {1,3,5,7,9};

# set()将字符串转为集合
word_set = set('abcde');

# set()将列表转为集合
week_set = set(['monday','tuesday','wednesday']);

# set()将元组转为集合
week_set = set(('monday','tuesday','wednesday'));

# set()将字典的键转为集合
week_set = set({'monday':'星期一','tuesday':'星期二','wednesday':'星期三'});

# in判断是否存在
is_exist = 'monday' in week_set;


a = {1,2,3};
b = {3,4,5};
# 交集运算
r = a & b;

# 并集运算
r = a | b;

# 差集运算
r = a - b;

# 异或运算
r = a ^ b;

# 判断是否为子集,本身可以为本身的子集
r = a.issubset(b);
r = a <= b;

# 判断是否为真子集
r = a < b;

# 判断是否为超集,本身可以为本身的超集
r = a.issuperset(b);
r = a >= b;

# 判断是否为真超集
r = a > b;

