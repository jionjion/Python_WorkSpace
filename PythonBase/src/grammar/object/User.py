# -*- coding: utf-8 -*-
   
# 一个常见的User类
# 默认继承了Object类,具有Object的特有的方法和属性

class User:
    
    #类的属性,全部对象可以使用修改
    desc = "这是用户类";                         
    
    #构造函数
    def __init__(self,name,sex,age):
        #对象的属性构造,每个对象均不相同,但是可以直接通过访问
        self.name = name;
        #类的特有属性,但是仍会被访问到
        self._sex = sex;    
        #类的私有属性,被解释器解析为其他名字,但仍能被访问到
        self.__age = age;
        pass;
    
    #被类方法修饰器修饰后,可以直接通过类名.方法名()进行调用
    @classmethod
    def say_hello(self):                                        #修饰的类,必须传入self形参
        print("hello");
    
    #属性方法修饰器修饰后,可以通过对象.方法名,不需要括号就可以进行调用
    @property
    def get__age(self):
        return self.__age;
    
    #析构函数,销毁时调用
    def __del__(self):      
        pass;
    

jion = User('Jion','男',19);

#打印类的类型
print("类的类型:",type(jion));                                      
#打印类的方法
print("类的属性和方法:",dir(jion));
#@classmethod修饰的类方法,可以直接通过类名.方法名()进行执行
User.say_hello();
#@property修饰的方法,可以通过对象名.方法直接执行获取
print("年龄:",jion.get__age);