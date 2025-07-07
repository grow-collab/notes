import pandas as pd
import numpy as np

# Series
ps = pd.Series(np.random.randn(12),index=[['a','a','a','b','b','b','c','c','c','d','d','d']])
# print(ps)
ps2 = pd.Series(np.random.randn(12),index=[['b','b','b','a','a','a','c','c','c','d','d','d'],[0,1,2,0,1,2,0,1,2,0,1,2]])
# print(ps2)
# print(ps2.index)
# print(type(ps2.index))

# Series 取值
# 取a这一组的数据
# print(ps2['a'])
# 指定取值
# print(ps2['a', 2])
# 各组数据内层索引为2的数据
# print(ps2[:, 2])

# 交换和排序 Series
# 交换--外层索引和内层索引进行交换
# print(ps2.swaplevel())

# Series 排序
ps2.index.names = ['key1','key2']
# print(ps2)
# print(ps2.sort_index())
# print(ps2.sort_index(level='key1',ascending=False))


# DataFrame 层级索引
pf = pd.DataFrame(np.arange(12).reshape((4, 3)),
                     index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                     columns=[['A','C','B'],
                              [0,1,2]])
print(pf)
pf.index.names = ['key1','key2']
pf.columns.names = ['x1','x2']
# 取列
# print(pf['A'])
# 取行值
# print(pf.loc['b'])
# 取指定的数据
# print(pf.loc[:, 'A'])

# 排序 索引排序 默认是行
# print(pf.sort_index(level='key1'))
# print(pf.sort_index(level='x1',axis=1))

# 值排序
print(pf.sort_values(by=[('B', 2),('A',0)],ascending=False))