import pandas as pd
import numpy as np

data = pd.DataFrame(np.random.randn(1000, 4))
print(data)

cond = (np.abs(data) > 2).any(axis=1)
print(cond)
print(data.loc[cond])
# data.loc[cond] = 3
print(data)

# 使用abs计算绝对值
abs_df = data.abs()
# 找出大于3的索引
bool_index = abs_df > 3
pos = np.where(bool_index)
print(pos)

idx_dict = {}
for r, c in zip(pos[0], pos[1]):
    idx_dict[r] = c
print(idx_dict)

# 修改异常值
for i in idx_dict.keys():
    data.iloc[i, idx_dict[i]] = 3
print(data)
print(data.describe())
