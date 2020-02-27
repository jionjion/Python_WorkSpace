# -*- coding: utf-8 -*-

'''
    redispy
        pip install redis
        pip install redispy
        doc http://redis-py.readthedocs.io/en/latest/

'''

import redis


class redisDML(object):
    def __init__(self):
        # 创建连接,默认使用0号分库
        self.redis = redis.StrictRedis(host='localhost', port=6379, db=0)

    # 字符Str相关操作
    def str_operation(self):
        # [set] 存入,修改单个
        self.redis.set(name='name', value='Jion')
        # [append]
        self.redis.append(key='name', value='!')
        # [get] 获得单个
        print(self.redis.get(name='name'))
        # [mset] 存入,修改多个值,传入字典类型
        self.redis.mset({'name1': 'Jion', 'name2': 'Arise'})
        # [mget] 获得多个值,传入列表类型
        print(self.redis.mget(['name1', 'name2']))
        # [del] 删除
        self.redis.delete('name')

    # 列表List相关操作
    def list_operation(self):
        # [lpush]/[rpush] 从左/右开始插入
        self.redis.rpush('names', 'Jion', 'Arise')
        # [lrange] 返回指定长度的字符
        print(self.redis.lrange(name='names', start=0, end=-1))
        # [ltrim] 截取指定长度,截取前两个
        self.redis.ltrim(name='names', start=0, end=1)
        # [lpop]/[rpop] 弹出最左/右的元素,删除并返回
        print(self.redis.lpop(name='names'))
        # [lpushx]/[rpushx] 如果列表存在,则在最左/右添加
        self.redis.lpush('names', 'Biob')

    # 集合Set相关操作
    def set_operation(self):
        # [sadd] 添加元素
        self.redis.sadd('names1', 'Jion', 'Arse', 'Mary')
        self.redis.sadd('names2', 'Biob', 'Arse')
        # [srem] 删除元素
        self.redis.srem('names1', 'Mary')
        # [sismember] 判断元素是否在集合内部
        print(self.redis.sismember(name='names1', value='Jion'))
        # [smembers] 返回所有的成员
        print(self.redis.smembers(name='names1'))
        # [sdiff] 差集
        print(self.redis.sdiff('names1', 'names2'))
        # [sinter] 交集
        print(self.redis.sinter('names1', 'names2'))
        # [sunion] 并集
        print(self.redis.sunion('names1', 'names2'))

    # 散列hash相关操作
    def hash_operation(self):
        # [hset] 设置散列的值,重复则覆盖 设置成功返回1,否则返回0. key唯一,作为区分
        print(self.redis.hset(name='users', key=1, value={'name': 'Jion', 'age': 24}))
        # [hget] 获取散列值
        print(self.redis.hget(name='users', key=1))
        # [hmset] 设置多个散列值,传入一个字典类型,设置成功返回True,否则返回False
        print(self.redis.hmset(name='users', mapping={2: {'name': 'Arise', 'age': 23}, 3: {'name': 'Biob', 'age': 22}}))
        # [hmget] 获取多个散列值,返回顺序取决于传入顺序
        print(self.redis.hmget(name='users', keys=[1, 2]))
        # [hsetnx] 如果散列已经存在, 则不进行覆盖, 也不添加,返回0
        print(self.redis.hsetnx(name='users', key=1, value={'name': 'jion'}))
        # [hkeys] 返回所有的主键
        print(self.redis.hkeys(name='users'))
        # [hvals] 返回所有的主键,域和值
        print(self.redis.hvals(name='users'))
        # [hlen] 返回散列包含的主键记录的数量
        print(self.redis.hlen(name='users'))
        # [hdel] 删除散列指定的域,成功删除返回1,否则返回0
        print(self.redis.hdel('users', [1]))
        # [hexists] 判断指定主键散列是否存在,在返回True,否则返回False
        print(self.redis.hexists(name='users', key=1))


if __name__ == '__main__':
    obj = redisDML()
    # obj.str_operation()
    # obj.list_operation()
    # obj.set_operation()
    obj.hash_operation()
