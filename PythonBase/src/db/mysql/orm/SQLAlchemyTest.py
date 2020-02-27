# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker

import datetime

# 获取连接,指定数据库字符集
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/python?charset=utf8mb4')

# 获取基类,数据模型类均继承该类
base = declarative_base()


# 声明数据模型,定义数据类型
class Book(base):
    # 基表
    __tablename__ = 'BOOK'

    # 数字字段类型,是否为主键
    id = Column(type_=Integer, primary_key=True)
    # 字符字段类型,且不为空
    name = Column(type_=String(200), nullable=False)
    author = Column(type_=String(200))
    # 日期类型
    publication_date = Column(type_=DateTime)

    # 重写描述方法
    def __repr__(self):
        return "<Book(id='%s', name='%s', author='%s', publication_date='%s' )>" \
               % (self.id, self.name, self.author, self.publication_date)


# 创建表,通过数据模型绑定数据库连接引擎
# Book.metadata.create_all(engine)

# 创建连接会话对象,并绑定数据库连接
Session = sessionmaker(bind=engine)


# 增删改查
class MysqlDML:
    # 初始化Session对象,作为类属性
    def __init__(self):
        self.session = Session()

    # 新增一条记录,并返回
    def add_one(self):
        # 创建对象
        book = Book(
            name='三体',
            author='刘慈宁',
            publication_date=datetime.datetime.now()
        )
        # 存入session中
        self.session.add(book)
        # 提交
        self.session.commit()
        return book

    # 批量提交
    def add_more(self):
        # 创建对象数组
        book1 = Book(
            name='银河帝国三部曲',
            author='艾萨克·阿西莫夫',
            publication_date=datetime.datetime.strptime('2001-01-01', '%Y-%m-%d')
        )
        book2 = Book(
            name='冰与火之歌',
            author='乔治·马丁',
            publication_date=datetime.datetime.strptime('1945-01-01', '%Y-%m-%d')
        )
        book_list = [book1, book2]
        # 存入,并提交事务
        self.session.add_all(book_list)
        self.session.commit()
        return book_list

    # 查询主键数据
    def get_one(self):
        # 获得主键为2的数据
        book = self.session.query(Book).get(2)
        return book

    # 条件查询
    def get_column(self):
        book_name = "三体"
        # 查询条件, 通过字段 name 过滤
        return self.session.query(Book).filter_by(name=book_name)

    # 模糊查询
    def get_like(self):
        return self.session.query(Book).filter(Book.name.like('%三%')).all()

    # 通过范围查询
    def get_in(self):
        return self.session.query(Book).filter(Book.id.in_([1, 2, 3])).all()

    # 通过日期范围查询
    def get_date(self):
        return self.session.query(Book).filter( datetime.datetime.strptime('2000-01-01', '%Y-%H-%d') < Book.publication_date , Book.publication_date <= datetime.datetime.now()).all()

    # 通过分页查询
    def get_page(self):
        return self.session.query(Book).limit(3).all()

    # 修改
    def modify_one(self):
        # 查询
        book = self.session.query(Book).get(2)
        # 修改内容,并保存
        book.name = '三体'
        self.session.add(book)
        # 提交事务
        self.session.commit()
        return book

    # 删除
    def delete_one(self):
        book = self.session.query(Book).get(18)
        if book:
            self.session.delete(book)
            self.session.commit()
            return book
        return None


# 测试
class MysqlDMLTest:
    """
        测试 ORM
    """
    if __name__ == '__main__':
        obj = MysqlDML()
        # 测试新增一条
        print(obj.add_one())
        # 测试批量提交
        print(obj.add_more())
        # 查询主键数据
        print(obj.get_one())
        # 测试条件查询
        print(obj.get_column())
        # 测试模糊查询
        print(obj.get_like())
        # 测试通过范围查询
        print(obj.get_in())
        # 测试通过日期范围查询
        print(obj.get_date())
        # 通过分页查询
        print(obj.get_page())
        # 测试修改
        print(obj.modify_one())
        # 测试删除
        print(obj.delete_one())

        # 通过点,调用内置方法. 查询属性,数量
        print(obj.get_one().name)
        print(obj.get_one().count())
