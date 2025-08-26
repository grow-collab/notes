from sqlalchemy import create_engine, text

# 配置信息
HOST_NAME = '127.0.0.1'
PORT = '3306'
USER_NAME = 'root'
PASSWORD = '123456'
DATABASE = 'yang_01'

# 配置选项
DB_URL = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USER_NAME, PASSWORD, HOST_NAME, PORT, DATABASE)
# dialect+driver://username:password@host:port/?charset=utf8

engine = create_engine(DB_URL)

with engine.connect() as con:
    result = con.execute(text('select * from test;'))
    for row in result:
        print(row)
