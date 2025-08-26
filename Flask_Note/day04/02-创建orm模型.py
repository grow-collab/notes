from sqlalchemy import create_engine, Column, Integer, String, func  # 导入数据库链接引擎
from constants import DB_URI
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(DB_URI)

# 创建base基本,所有的模型类都要继承这个基类
Base = declarative_base()


# 创建orm模型 ==> 对象
class User(Base):
    # 定义表名
    __tablename__ = 'users'
    # 创建字段
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(50))
    age = Column(Integer, default=18)

    def __repr__(self):
        return f'{self.name}的User模型'


# 映射模型
# 先删除表,在创建表
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
# 数据迁移


# 获取数据库管理员
session = sessionmaker(bind=engine)()

# 添加数据到表中

# 1.添加单条数据
# one_user = User(name='张三', fullname='法外狂徒', password='666666')
# # 对数据库的相关操作,需要数据库管理员来做
# session.add(one_user)
# session.commit()

# 2.添加多条数据
one_user = User(name='张三', fullname='法外狂徒', password='666666')
two_user = User(name='诡术妖姬', fullname='乐芙兰', password='888888', age=30)
three_user = User(name='影流之主', fullname='劫', password='999999', age=45)
session.add_all([one_user, two_user, three_user])
session.commit()

# 3.查找数据
# result = session.query(User).all()
# print(result)  # sql语句

# 条件查询
# result = session.query(User).filter_by(name='张三').all()
# print(result)

# result = session.query(User).filter(User.age > 18).all()
# print(result)


# result = session.query(User).get(2)
# print(result)

# 取出结果集第一条数据
# result = session.query(User).first()
# print(result)




# 修改数据
# result = session.query(User).first()
# result.password = '111111'
# session.commit()

# 删除数据
# result = session.query(User).first()
# session.delete(result)
# session.commit()


# query的可用参数(func)
# 统计数据
# age = session.query(func.count(User.age)).all()
# print(age)

# 平均值
# nums = session.query(func.avg(User.age)).all()
# print(nums)

# 最大值
# nums = session.query(func.max(User.age)).all()
# print(nums)
#
# # 最小值
# nums = session.query(func.min(User.age)).all()
# print(nums)
#
# # 求和
# nums = session.query(func.sum(User.age)).all()
# print(nums)

# 排序
# result = session.query(User).order_by(User.age).all()
# print(result)
#
# result = session.query(User).order_by(-User.age).all()
# print(result)

# 切片 [:2]
# result = session.query(User).all()[:2]
# print(result)


# 表关系 ==> 外键
# 一对一
# 一对多
# 多对多
