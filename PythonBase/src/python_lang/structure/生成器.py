# 生成器是用来创建 Python 序列的一个对象。使用它可以迭代庞大的序列，且不需要在内存中创建和存储整个序列。

# 生成[0,100)的自然数序列
range(0,100);

# 自定义生成器
def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number;               # 修改序列中该元素
    number += step