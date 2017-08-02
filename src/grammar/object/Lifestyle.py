# -*- coding: utf-8 -*-

# 类的生命周期
class Lifestyle():
    
#     def __new__(self):
#         print("执行new初始化方法....");
    
    def __init__(self,name,age):
        self.name = name;
        self.age = age;
        pass;
        
    def say_hello(self):
        print("hello");
        
    #比较运算符    
    def __cmp__(self):
        pass;
    
    #等于运算符
    def __eq__(self,other):                             #传入对象other
        if isinstance(other, Lifestyle):                #如果类类型一致,则比较属性
            if self.age == other.age:                   #如果属性一直,则认为类相等
                return True                             #返回真
            else:
                return False
        else:
            return False                                #类型不一致,返回假
    
    #小于
    def __lt__(self):
        pass;
    
    #大于
    def __gt__(self):
        pass;
        
    #加    
    def __add__(self,other):                            #传入其他对象,将other对象的age属性值加于本身
        if isinstance(other, Lifestyle):                #判断类型是否相同
            return self.age + other.age;                #属性相加
        else:
            raise Exception("类型不匹配")                  #抛出异常
    
    #减
    def __sub__(self):
        pass;
    
    #乘
    def __mul__(self):
        pass;
    
    #除
    def __div__(self):
        pass;    
    
    #且  
    def __and__(self):
        pass;
    
    #或  
    def __or__(self):
        pass;
    
    #将类转为人易看懂的
    def __str__(self):
        return "对象为: %s ,年龄: %s" % (self.name,self.age);    #可以使用%结合前后进行占位符
    
    #转为机器语言
    def __repr__(self):
        return self.__diet__.key();
    
    #字符编码
    def __unicode__(self):
        pass;
    
    #设置属性
    def __setattr__(self,name,value):
        self.__dict__[name] = value;
    
    #获取属性
    def __getattribute__(self,name):
        return super(Lifestyle,self).__getattribute__(name);
    
Jion = Lifestyle("Jion",10);
Arise = Lifestyle("Arise",10);

print("是否相等:",Jion.__eq__(Arise));
print("是否相等:",Jion==Arise);
# print("相加:",Jion+Arise);
print(Jion);                                                #打印自我描述
print(dir(Jion))                                            #打印定义属性
# 设置属性
Jion