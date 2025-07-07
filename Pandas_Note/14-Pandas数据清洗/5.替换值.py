import pandas as pd
import numpy as np

ps = pd.Series(np.arange(20, 30))
# print(ps)
# 标签索引
# ps.loc[0] = 888
# print(ps)
# 表达式 比较运算符
# ps.loc[ps % 2 == 0] = 999
# print(ps)
# 如果直接写的是一个对象进行比较 会替换对应的值
# 如果直接使用值比较 会多出一行
# ps.loc[ps[9] >= 29] = 888
# print(ps)

# 可以通过map或者apply方法进行
# print(ps.map(lambda x: x * 1000))
# print(ps.apply(lambda x: x * 1000))

# ps<=25, true 26,27,28,29 都是为False 所以改变的是False的值
# data1 = ps.where(ps < 25, -1)
# print(data1)

'''
replace(1,2,3)
    1.to_replace 要替换的值或者是一个字典
    2.values 替换后的新值
    3.inplace 是否在源对象上进行修改
'''
df = pd.DataFrame(ps)
print(df)
df.replace(26, np.nan, inplace=True)
print(df)
df.replace({23: 999, 27: np.nan}, inplace=True)
print(df)
df.replace([29, 20], [30, 19], inplace=True)
print(df)
