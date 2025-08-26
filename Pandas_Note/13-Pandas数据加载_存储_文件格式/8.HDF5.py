import pandas as pd
import numpy as np

pd1 = pd.DataFrame({'a':np.random.randn(100)})
# print(pd1)

hdf = pd.HDFStore('hdf5.h5')
# 如果报错 通过pip 下载tables

# 添加
hdf['pd'] = pd1
# print(hdf['pd'])

# 两种存储模式 fixed table:比较慢
hdf.put('obj2',pd1,format='table') # 这种方式就相当于hdf['pd'] = pd1
# print(hdf['obj2'])

# 查询
# print(hdf.select('obj2', where=['index>=10 and index<=15']))

# 将DataFrame保存为HDF5的格式
pd1.to_hdf('test.h5',key='test',mode='w')

pd2 = pd.read_hdf('test.h5')
print(pd2)