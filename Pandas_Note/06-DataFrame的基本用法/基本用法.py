import pandas as pd
import numpy as np

# 1.T转置,将行和列索引位置交换 行 <-> 列
data = np.arange(9).reshape(3,3)

pf = pd.DataFrame(data,index=['a','b','c'],columns=['A','B','C'])
print(pf)

pf2 = pf.T # T转置
# print(pf2)


# 2.通过列索引获取列数据
print(pf['A']) # 获取一列数据

column_index = ['A','C'] # 获取多列数据
print(pf[column_index])


# 3. 增加列数据
pf['D'] = [1,3,10]
print(pf)

# 4.删除列
del pf['B']
print(pf)