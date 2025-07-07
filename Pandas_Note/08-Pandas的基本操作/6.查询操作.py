import pandas as pd
import numpy as np

# Series
# d.查询
ps = pd.Series(np.arange(6),index=['a','b','c','d','e','f'])
# print(ps)

# 1.通过索引查询
# print(ps['a'])

# 2.多数据查询
# 位置切片索引
# print(ps[1:3])
# 标签切片
# print(ps['a':'d'])
# 不连续索引
# print(ps[['a', 'f']])
# 布尔索引 算术运算符 比较运算符
# print(ps[ps > 2])


# DataFrame
# d.查询
pf = pd.DataFrame(np.arange(9).reshape(3,3),index=['a','b','c'],columns=['A','B','C'])
print(pf)
# 列索引
print(pf['A'])
# 取多列
print(pf[['A', 'B']])

# 选取一个值
print(pf['A']['a'])
# 切片
print(pf[:2]) # 获取行