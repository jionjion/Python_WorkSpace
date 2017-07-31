# 创建一个类
class Person(object):                             #类名,继承object类
#创建类的构造方法
    def __init__(self, name, gender):             #第一个形参必须为self,但是在构造时不用传入
        self.name = name
        self.gender = gender
        self.__job = 'student'                    #双下划线修饰,为私有属性,外部无法访问    
#创建类的属�??
    describe = "这是类的属性,所有实例都可以修改";          #注意缩进
#创建类的方法
    @classmethod                                 #使用注解,标注为这是类方法,可以通过类型.方法名进行调用
    def self_introduction(self):                 #注意缩进
        return "自我介绍方法,为类方法";
    
#创建实例方法
    def get_job(self):                           #传入self,代表对象本身  
        return self.__job;                       #返回对象的__job私有属性

#创建类的实例,有参的构造方法
tom = Person('汤姆猫','喵');
#创建类的实例,无参的构造方法
jion = Person('Jion','男');                      #有参的构造方方法,会覆盖无参的构造方法

#动态语法,属性直接绑定
jion.address = "上海";                            #属性绑定时不用每个对象都必须拥有相同的全部

#### 
#访问类的属性
print(Person.describe);
#调用类方法
print(Person.self_introduction());
#通过实例方法,获取私有属性
print(jion.get_job());
