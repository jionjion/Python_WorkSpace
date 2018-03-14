# -*- coding: utf-8 -*-
'''
    Hashable   可以计数的哈希对象,用来计算对象出现的次数
'''
from collections import Counter

if __name__ == '__main__':
    # 这三种方式,用来统计每个元素出现的次数,效果相同
    print(Counter(['a', 'b', 'b', 'c', 'c', 'c']))
    print(Counter({'a': 1, 'b': 2, 'c': 3}))
    print(Counter(a=1, b=2, c=3))

    # [update]传入列表或者字典,在原有的基础上进行追加统计
    c = Counter(['a','b','c'])
    c.update('abc')                     # 追加统计
    c.update(['a','b','c'])             # 追加统计
    c.update({'a':1,'b':1,'c':1})       # 追加统计
    c.update(a=1,b=1,c=1)               # 追加统计
    print(c)

    # 例如:统计一句话中,abcde出现的次数
    c = Counter('abbcccddddeeeee')
    # 遍历统计
    for letter in 'abcde':
        # 使用 .[元素]的方式,获得该元素出现的次数
        print('%s 出现 %s' % (letter,c[letter]))
    # 统计出现次数最多的两个
    for letter, count in c.most_common(2):
        print('{} 最多出现 {}'.format(letter, count))

    # 统计计算,计算两组出现的和,差,交,并
    c1 = Counter(['a','b','b','c','c'])     # a=1 b=2 c=2
    c2 = Counter(['c','d','d','d','d'])     # c=1 d=4

    # 和 每个元素的出现的次数进行累计
    print(c1 + c2)                          # a=1 b=2 c=3 d=4
    # 差 前者出现的次数减去后者出现的次数,小于0则不显示
    print(c1 - c2)                          # a=1 b=2 c=1
    # 交 两者共同出现的元素,取最小
    print(c1 & c2)                          # c=1
    # 并 两者任意出现的元素,次数取最大
    print(c1 | c2)                          # a=1 b=2 c=2 d=4
