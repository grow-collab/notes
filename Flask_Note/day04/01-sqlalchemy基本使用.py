# sqlalchemy  ==> orm模型(对象) ==> sql语句
# pymysql
from sqlalchemy import create_engine,text  # 导入数据库链接引擎

# 数据库的配置
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'yang_01'
USERNAME = 'root'
PASSWORD = '123456'

# 配置选项
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
# dialect+driver://username:password@host:port/database?charset=utf8

engine = create_engine(DB_URI)

# 直接写SQL
# 创建链接
with engine.connect() as con:
    result = con.execute(text('select * from test;'))
    print(result.fetchall())
