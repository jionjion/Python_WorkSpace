# 推导式是从一个或者多个迭代器中快速创建数据结构的方法

# 列表推导表达式
# 语法      [ expression for item in iterable if condition]

# 10以内的偶数
number_list = [number*2 for number in range(0,5)];      
number_list = [number for number in range(0,10) if number % 2 == 1];    

# 多维度推导表达式 
cells = [(row, col) for row in range(0,5) for col in range(0,5)];


# 字典推导表达式
# 语法    { key_expression : value_expression for expression in iterable }

# 统计单词中字母出现的次数
word = 'hello join'
letter_counts = {letter: word.count(letter) for letter in set(word)}

# 集合推导式
# 语法    { expression for expression in iterable }

# 10以内除3余1
number_set = {number for number in range(1,10) if number % 3 == 1}

# 元组没有推导表达式,但是可以通过list列表转化
