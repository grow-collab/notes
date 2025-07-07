import pandas as pd
import numpy as np
"""
方法              说明
count           ⾮NA值的数量
describe        针对Series或各DataFrame列计算汇总统计
min,max         计算最⼩值和最⼤值
idxmin、idxmax  计算能够获取到最⼩值和最⼤值的索引值
quantile        计算样本的分位数（0到1）
sum             值的总和
mean            值的平均数
median          值的算术中位数(50%分位数)
var             样本值的⽅差
std             样本值的标准差
cumsum          样本值的累计和
"""
# 统计计算
pf = pd.DataFrame(np.random.randn(10).reshape(5,2),index=list('abcde'),columns=list('AB'))
pf.loc['a','B'] = np.nan
pf.loc['d','A'] = np.nan
# print(pf)
# 1.count ⾮NA值的数量
# print(pf.count()) # 默认是列,可以通过axis调整
# print(pf.count(axis=1))

# 2.describe 针对Series或各DataFrame列计算汇总统计
# print(pf.describe())

# 3.min,max 计算最⼩值和最⼤值
# print(pf.min()) # 最小值
# print(pf.max()) # 最大值
# print(pf['A'].max())

# 4.idxmin、idxmax 计算能够获取到最⼩值和最⼤值的索引值
# print(pf.idxmin()) # 最小值索引
# print(pf.idxmax(axis=1)) # 最大值索引,默认是计算列,可通过axis调整

# 5.quantile 计算样本的分位数（0到1）
# print(pf.quantile(axis=1))
# print(pf['A'].quantile())

# 6.sum 值的总和
# print(pf.sum)
# print(pf.sum(skipna=True,axis=1))
# print(pf['A'].sum())

# 7.mean 值的平均数
# print(pf.mean())

# 8.median 值的算术中位数(50%分位数)
# print(pf.median())

# 9.var:样本值的⽅差,std:样本值的标准差
# print(pf.var())
# print(pf.std())

# cumsum:样本值的累计和
ps = pd.Series([1,2,3,4,5])
print(ps)
print(ps.cumsum())