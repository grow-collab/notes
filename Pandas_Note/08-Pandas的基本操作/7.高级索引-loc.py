import pandas as pd
import numpy as np

# Series 标签索引loc
ps = pd.Series(np.arange(6),index=['a','b','c','d','e','f'])
print(ps['a':'e'])
print(ps.loc['a':'e'])


# DataFrame 标签索引loc
pf = pd.DataFrame(np.arange(9).reshape(3,3),index=['a','b','c'],columns=['A','B','C'])
print(pf)
# 标签切片
print(pf.loc['a':'b', 'C']) # 第⼀个参数是⾏ 第⼆个是列
print(pf.loc['a':'b', 'A':'B'])
