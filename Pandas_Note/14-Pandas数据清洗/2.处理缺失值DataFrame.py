import pandas as pd
import numpy as np

# # DataFrame
# df = pd.read_csv('数据/bus.csv',encoding='gbk')
# # print(df)
#
# # 判断是否存在缺失值,
# print(df.isnull())
#
# # 过滤/滤除缺失值
# # how='all',根据行进行 除非一整行都是缺失值数据才会被移除,否则将保留
# print(df.dropna(how='all'))
#
# # 将缺失值设置为指定值
# print(df.fillna(1))
#
# print(df.dropna(how='all',axis=1))


# 观察参数
df1 = pd.DataFrame(np.random.randn(7, 3))
df1.iloc[:4, 1] = np.nan
# print(df1)
df1.iloc[:2, 2] = np.nan
# print(df1)
# 删除缺失值等于2 的 缺失值
# 仅保留⾄少具有2个⾮NA值的⾏
# print(df1.dropna(thresh=2))

# 填充缺失数据
# pd2 = df1.fillna(0) # 返回的是一个新的对象
# print(pd2)
# inplace 对源数据进行修改 True 默认为False 返回的是一个新的对象
# df1.fillna(0, inplace=True)
# print(df1)

# print(df1.fillna({1: 0.2, 2: 0.9}))


# ffill 和 bfill
pd2 = pd.DataFrame(np.random.randn(6, 3))
# print(pd2)
pd2.iloc[2:, 1] = np.nan
pd2.iloc[4:, 2] = np.nan
print(pd2)

# ffill 根据上一行的数据填充缺失,默认为行,可以通过axis调整
# print(pd2.ffill(axis=1))

# bfill 根据后一行/一列的数据填充缺失
print(pd2.bfill())
