# -*- coding: utf-8 -*-
'''
    deque 双向队列
        线程安全的容器元素
'''

from collections import deque

if __name__ == '__main__':
    # 使用构造函数,构造双向队列对象   maxlen 限制最大的队列长度
    d = deque(['b','c','e'],maxlen=20)

    # 获得队列的长度
    len(d)
    # 获得第一个
    d[0]
    # 获得倒数第一个
    d[-1]
    # 删除元素 'c'
    d.remove('c')

    # [extend] 向队尾添加元素,可以传入数组,添加多个到队尾
    d.extend(['f','g'])
    # [append] 向队尾添加元素,只能添加一个,如果传入数组将作为对象,置于队尾
    d.append(['h','i'])

    # [extendleft] 向队首添加元素,可以传入多个元素,多次添加
    d.extendleft('a')
    # [appendleft] 向队首添加元素,一次只能添加一个
    d.appendleft('0')

    # 当前队列
    print(d)

    # 消费 [pop] 弹出队尾元素
    print(d.pop())
    # [popleft] 弹出队首元素
    print(d.popleft())

    # [rotate] 平移.因为队列可以双向移动,这里可以任意对队列元素进行平移操作
    d = deque(range(10))
    print('正常               :', d)

    d = deque(range(10))
    d.rotate(2)
    print('向右平移2单位      :', d)

    d = deque(range(10))
    d.rotate(-2)
    print('向左平移2单位      :', d)