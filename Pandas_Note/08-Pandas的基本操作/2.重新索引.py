import pandas as pd
import numpy as np

# 重新索引是指在 Pandas 中对现有的数据结构（如 Series、DataFrame）进⾏重新排序、添加、删除索引的操作。
# reindex,创建⼀个新的对象，⽽不改变原始数据
pf = pd.Series(np.arange(6),index=['a','b','c','e','f','g'])
print(pf)
# pf2 = pf.reindex(['A','B','C','D','E','F','G'])
pf2 = pf.reindex(['a','b','c','e','f','g','h'])
print(pf2)


pf1 = pd.DataFrame(np.arange(9).reshape(3,3),index=['a','b','c'],columns=['A','B','C'])
print(pf1)
# 行索引重建
pf4 = pf1.reindex(['a','b','c','d'])
# 列索引重建
pf5 = pf1.reindex(columns=['C','B','A'])
print(pf4)
print(pf5)

