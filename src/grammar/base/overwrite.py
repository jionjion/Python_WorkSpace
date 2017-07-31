#重写object类的默认方法
class Person(object):
    
    __slots__ = ('name', 'gender', 'score');                        #定义所有可用属性
     
    def __init__(self, name, gender):                               #重写构造方法,传入初始化参数
        self.name = name
        self.gender = gender
        
    def __str__(self):                                              #重写特殊方法,将用对象信息返回
        return '(Person: %s, %s)' % (self.name, self.gender)        #%百分号为占位符,其后拼接
    
    def __cmp__(self, s):                                           #重写比较方法,名字从a-z进行排序    
        if self.name < s.name:
            return -1
        elif self.name > s.name:
            return 1
        else:
            return 0
        
    def __len__(self):                                              #从写计算方法.根据传入的对象的name的长度进行计算
        return len(self.name);
        
    def __call__(self, friend):                                     #将对象转为函数对象,可以通过传入参数,完成方法的调用
        print ("将对象转为函数方法,获得传入参数:",friend);                      
    
jion = Person('Jion','男');                                          #创建实例          

print("用户信息:",jion);                                               #打印实例的信息
print("用户名长度:",len(jion));                                         #重写后的长度计算方法
jion("元素一");                                                        #将对象转为函数对象,执行有参的方法

