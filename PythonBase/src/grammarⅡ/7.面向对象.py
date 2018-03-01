# -*- coding: utf-8 -*-

类与对象

定义一个类,首字母大写,驼峰命名

class People:
    def __init__(self):
        print('父类实例化...')

    def do_homework(self):
        print('父类的do_homework方法')

# 定义一个继承类,可以有多继承
class Student(People):
    # 定义类变量
    age = 24
    tol = 1

    # 构造函数,空返回值.实例化时调用,可以单独调用
    def __init__(self , age):
        # 显示调用父类的构造方法
        super(Student,self).__init__()
        # 实例变量,使用self来为实例变量赋值
        self.age = age
        # 类变量,通过__class__来访问类变量,对类 变量进行操作,所有实例中的类变量均会修改
        self.__class__.tol += 1
        # 变量控制
        self.score = 0
        print('Student类实例化...')

    # 定义实例方法,参数列表首个为self,使用self表示调用者本身,为实例变量赋值
    def print_name(self , name):
        print('name:', name , 'age:' , self.age)

    # 定义私有方法,__开头
    def __private_method(self):
        print('类的私有方法!')

    # 定义类方法
    @classmethod
    def class_method(cls):
        print('这是学生类的类方法!')

    # 定义静态方法,没有指带对象,如self,cls
    @staticmethod
    def static_method():
        print('这是学生类的静态方法!')

    # 实例变量保护
    def mark_score(self , score):
        if score <= 0:
            score = 0

        # 赋值语句,避免成员变量随意更改
        self.score = score
        print('打分:' , score)

    # 方法的重载
    def do_homework(self):
        super(Student,self).do_homework()
        print('子类的do_homework方法')




实例化对象
student = Student()
student = Student(20)
student.print_name('Jion')

访问类变量
print(Student.age)

一般是通过 from 模块 import 类名 在另外模块中调用

打印对象的变量信息,首先打印实例信息,如果没有打印类信息
print(student.__dict__)

继承:避免重复的属性和方法
