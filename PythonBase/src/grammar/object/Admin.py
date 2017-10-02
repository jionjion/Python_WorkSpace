# -*- coding: utf-8 -*-
from grammar.object.User import User

# 继承自User类,重写其中的部分方法
class Admin(User):
    
    #重写父类的方法
    def __init__(self,name,sex,age,address):
        super(Admin, self).__init__(name,sex,age);                              #调用父类的构造方法,传入子类构造函数方法的参数
        self.address = address;                                                 #将多余的构造参数进行赋值

        
#创建子类
admin = Admin("admin","未知","18","上海");  
print("子类的方法:",dir(admin));
admin.__dict__;
print("子类的种类:",type(admin));
print("子类是否属于本身:",isinstance(admin, Admin));

