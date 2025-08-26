import pandas as pd
from sqlalchemy import create_engine

# Mysql配置信息
MYSQL_USER = 'root'
MYSQL_PS = '123456'
MYSQL_HOST = 'localhost'
MYSQL_DB = 'yang_01'
MYSQL_PORT = 3306

# 连接信息
mysqlengine = create_engine(f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PS}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}?charset=utf8')
# 查询
sql_query = 'SELECT *FROM test'
df = pd.read_sql(sql_query,mysqlengine)
# print(df)
df['sex'] = [99,95,91]
print(df)
# if_exists = 'fail' fail:什么都不做     replace 重写,append 追加
# df.to_sql('test',mysqlengine,if_exists='replace',index=False)

df1 = pd.read_sql(sql_query,mysqlengine)
print('-----------')
print(df1)
df1.loc[4] = [0,3,4,'lll',87,9]
# df1.to_sql('test',mysqlengine,if_exists='append',index=False)
# print(df1)

df2 = pd.DataFrame({
    'id':[99],
    'name':['安琪拉'],
    'age':[26],
    'sex':[22]
})
df2.to_sql('test',mysqlengine,if_exists='append',index=False)