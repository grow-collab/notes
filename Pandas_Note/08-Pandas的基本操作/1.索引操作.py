import pandas as pd
import numpy as np

# 1. Series和DataFrame中的索引都是index对象
pf = pd.Series(np.arange(6),index=['a','b','c','d','e','f'])
print(pf)
print(type(pf.index))

pf2 = pd.DataFrame(np.arange(9).reshape(3,3),index=['a','b','c'],columns=['A','B','C'])
print(pf2)
print(type(pf.index))


# 2. 索引对象不可变,保证了数据的安全
print(pf2.index)
pf2.index['C'] = 2 # TypeError: Index does not support mutable operations
pf2.index['a'] = 'n'
print(pf2)


# 3. 常⻅的index的种类
# a. index , 索引
# b. int64index, 整数索引
# c. MultiIndex, 层级索引
# d. DatatimeIndex 时间戳索引