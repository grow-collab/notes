import pymysql

# 数据库的链接对象
conn = pymysql.connect(host='127.0.0.1', user='root', password='root', database='mysite', charset='utf8')
# 获取光标对象
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 以字典的方式返回查询出来的数据

# 写sql语句
