import numpy as np
import pandas as pd

# 创建⼀个多重索引的Series
data = pd.Series(np.random.randn(9), index=[['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'],
                                            [1, 2, 3, 1, 3, 1, 2, 2, 3]])
# 显示Series
print(data)
# 选择外层索引为'a'的⼦集
print(data['a'])
# 切⽚,选择'b'⾄'c'索引之间的⼦集
print(data['b':'c'])
# 通过loc选择多重索引的⼦集,选择外层索引为'b','d'的⾏
print(data.loc[['b', 'd']])
# 通过loc选择多重索引的⼦集,选择内层索引为2的元素
print(data.loc[:, 2])

# DataFrame
frame = pd.DataFrame({'a': range(7), 'b': range(7, 0, -1),
                      'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'],
                      'd': [0, 1, 2, 0, 1, 2, 3]})
# 显示DataFrame
print(frame)
# 设置多重索引,外层索引为'c','d',内层保持原索引
frame2 = frame.set_index(['c', 'd'])
# 显示设置了多重索引的DataFrame
print(frame2)
# 设置多重索引,外层索引为'c','d',但保留原索引列
# frame2 = frame.set_index(['c','d'], drop=False)
# 重置索引,移除多重索引,恢复原索引
print(frame2.reset_index())
