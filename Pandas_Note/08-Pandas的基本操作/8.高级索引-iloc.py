import pandas as pd
import numpy as np

# Series 位置索引iloc
ps = pd.Series(range(5),index=["a","b","c","d","e"])
print(ps)
print(ps[1:3]) # 包头不包尾
print(ps.iloc[1:3]) # 推荐iloc这种操作


# DataFrame 位置索引iloc
pf = pd.DataFrame(np.arange(9).reshape(3,3),index=['a','b','c'],columns=['A','B','C'])
print(pf)
print(pf.iloc[:, 0:2]) # 第⼀个参数是⾏ 第⼆个是列