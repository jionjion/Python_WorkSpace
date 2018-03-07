# -*- coding: utf-8 -*-

'''
使用字典代替switch
'''

# 自定义函数句柄
def get_sunday():
    return 'Sunday'

def get_monday():
    return 'Monday'

def get_tuesday():
    return 'Tuesday'

def get_default():
    return 'None'

# 默认执行函数
switcher = {
    0 : get_sunday,
    1 : get_monday,
    2 : get_tuesday
}

day = 8
# day_name = switcher[day]
# get()方法,获得字典的值,如果找不到返回默认值
day_name = switcher.get(day ,get_default)()

print(day_name)

'''
    使用列表推导式
    对a列表的数字求其平方
    [],{}可以完成对列表,集合进行推导
'''
a = [1,2,3,4]
# 使用列表推导式,完成对新偶数数字的立方
b = [i**3 for i in a if i%2==0]
print(b)


'''
    对自定义的对象进行判断空值
    __bool__ 和 __len__ 方法,决定对象是否存在
'''
class Student():
    pass

    # 间接判断是否存在,只能返回数字
    def __len__(self):
        return 0

    # 直接决定,对象是否存在,只能返回布尔值
    def __bool__(self):
        return True

# 判断数据是否存在
print(bool(Student()))
