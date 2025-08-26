import pandas as pd
import numpy as np

# 1. 数组,列表或者元祖构成的字典创建DataFrame
# 使用数组创建,字典的关键字为列索引,行索引自动生成
# data = {
#     'A':np.arange(1,6),
#     'B': np.arange(1, 6),
#     'C': np.arange(1, 6),
# }
# pf = pd.DataFrame(data)
# print(pf)

# 使用列表构成的字典创建
# data = {
#     'A':[1,2,3,4],
#     'B':[5,6,7,8],
#     'C':[9,10,12,6]
# }
# pf1 = pd.DataFrame(data)
# print(pf1)

# 使用元组
# data = {
#     'A':(1,2,3,4),
#     'B':(5,6,7,8),
#     'C':(9,10,12,6)
# }
# pf2 = pd.DataFrame(data)
# print(pf2)


# 2.Series构建的字典来创建DataFrame
# data = {
#     'A':pd.Series([1,2,3,4,5]),
#     'B': pd.Series([1, 2, 3, 4, 5]),
#     'C': pd.Series([1, 2, 3, 4, 5]),
# }
# pf = pd.DataFrame(data,index=range(0,5),columns=['A','B','C'])
# print(pf)
# # 查看行索引
# print(pf.index)
# # 查看列索引
# print(pf.columns)
# # 查看vlaues
# print(pf.values)


# 3. 字典构成的字典来创建DataFrame
# 注意:在创建DataFrame时, 外层字典key将成为列索引/列标签,内层字典中的key成行索引
data = {
    "A": {'a': 1, "b": 2, "c": 3},
    "C": {'a': 4, "b": 5, "c": 6},
    "B": {'a': 7, "b": 8, "c": 9},
}
pf = pd.DataFrame(data)
print(pf)