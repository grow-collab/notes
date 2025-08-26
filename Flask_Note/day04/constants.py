# 常量
# 数据库的配置
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'test'
USERNAME = 'root'
PASSWORD = '123456'

# 配置选项
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
# dialect+driver://username:password@host:port/database?charset=utf8
