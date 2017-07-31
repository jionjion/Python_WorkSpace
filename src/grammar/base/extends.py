#使用继承完成
#创建父类
class Person(object):
    def __init__(self, name, password):                         #父类的构造方法
        self.name = name
        self.password = password
        
#创建子类        
class Student(Person):                                          #继承父类,可以传入多个父类,完成多个继承
    def __init__(self, name, gender, score):                    #重写构造方法
        super(Student, self).__init__(name, gender)             #super调用父类的构造方法,传入初始化参数
        self.score = score                                      #子类新增的构造方法补充


jion = Student("Jion","男","100");
print("jion是不是Person类的实例:",isinstance(jion, Person))

#获取对象类型
print("jion对象类型:",type(jion));
print("jion对象属性有:",dir(jion));
