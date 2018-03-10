# -*- coding: utf-8 -*-
'''
    使用ORM完成关系对象映射
    技术实现
        SqlObject
        peewee
        Django's ORM
        SQLAlchemy
    这里使用
        pip install SQLAlchemy
'''

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,DateTime,Boolean
from sqlalchemy.orm import sessionmaker

# 获取连接,指定数据库字符集
engine = create_engine('mysql://root:123456@localhost:3306/python?charset=utf8')

# 获取基类
base = declarative_base()

# 声明模型,定义数据类型
class News(base):
    # 基表
    __tablename__ = 'news'

    # 字段类型
    id = Column(type_=Integer,primary_key=True)
    title = Column(type_=String(200),nullable=False)
    content = Column(type_=String(200),nullable=False)
    type = Column(type_=String(200),nullable=False)
    image = Column(type_=String(200))
    author = Column(type_=String(20))
    view_count = Column(type_=Integer)
    create_date = Column(type_=DateTime)
    is_valid = Column(type_=Boolean)

# 创建表
News.metadata.create_all(engine)

# 创建连接方法,并绑定数据库连接
Session = sessionmaker(bind=engine)

'''
    增删改查
'''
class DML(object):
    # 初始化Session对象
    def __init__(self):
        self.session = Session()

    # 新增一条记录
    def add_one(self):
        # 创建对象
        new = News(
            title = '标题',
            content = '内容',
            type = '类型'
        )
        # 存入session中
        self.session.add(new)
        # 提交
        self.session.commit()
        return new

    # 批量提交
    def add_more(self):
        # 创建对象数组
        new1 = News(
            title='标题',
            content='内容',
            type='类型'
        )
        new2 = News(
            title='标题',
            content='内容',
            type='类型'
        )
        news_list = [new1,new2]
        # 存入,并提交事务
        self.session.add_all(news_list)
        self.session.commit()
        return news_list

    # 查询主键数据
    def get_one(self,id):
        # 获得第一条数据
        new = self.session.query(News).get(id)
        return new

    # 条件查询
    def get_type(self,type):
        # 查询条件
        return self.session.query(News).filter_by(type=type)

    # 修改
    def modify_one(self,id):
        # 查询
        new = self.session.query(News).get(id)
        # 修改内容后添加
        new.author = 'Jion'
        new.view_count = 1
        self.session.add(new)
        # 提交事务
        self.session.commit()
        return new

    # 删除
    def delete_one(self,id):
        new = self.session.query(News).get(id)
        self.session.delete(new)
        self.session.commit()
        return new

if __name__ == '__main__':
    obj = DML()
    # print(obj.add_one())
    # print(obj.add_more())
    # print(obj.get_one(2).title)     # 通过点,进而查询对象属性
    # print(obj.get_type('类型').count())   # 通过点,调用内置方法
    # print(obj.modify_one(1))
    print(obj.delete_one(3))