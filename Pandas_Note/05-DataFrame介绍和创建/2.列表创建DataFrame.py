import pandas as pd
import numpy as np

# 1. 2D ndarray创建DataFrame
data = np.array([[1, 2, 3], [4, 5, 6], [9, 8, 7]])
# print(data)
pf = pd.DataFrame(data)
print(pf)


# 2. 字典构成的列表创建DataFrame
# data = [
#     {"name": "龙仔", "性别": "男", "年龄": 18},
#     {"name": "小龙仔", "性别": "男", "年龄": 18},
#     {"name": "宝宝", "性别": "女", "年龄": 18},
# ]
# pf1 = pd.DataFrame(data)
# print(pf1)


# 3. Series构成的列表创建DataFrame
# data = [
#     pd.Series([1,2,3]),
#     pd.Series([4, 5, 6]),
#     pd.Series([7, 8, 9])
# ]
# pf2 = pd.DataFrame(data)
# print(pf2)