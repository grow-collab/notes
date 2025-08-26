import numpy as np
import pandas as pd

# 1.离散化
# 创建待离散化的数据
# data = np.arange(1, 101)
# print(data)
# # 设置区间数量
# n_bings = 5
#
# # 计算数值范围
# min_val, max_val = np.min(data), np.max(data)
# print(min_val, max_val)
# # 计算宽度
# bin_width = (max_val - min_val) / n_bings
# print(bin_width)
# # 等宽离散化
# bins = np.arange(min_val, max_val, bin_width)
# print(bins)
# # 利用np.digitize等宽离散化
# discrete_data = np.digitize(data, bins)
# print(discrete_data)

# 2.面元划分
ages = [19, 22, 25, 27, 28, 29, 31, 37, 61, 45, 32, 91]
# 指定面元区间端点
bisn = [18, 25, 35, 60, 100]
# 面元化
cats = pd.cut(ages, bisn)
print(cats)
print(cats.codes)
print(cats.categories)
# 设置面元的左右开闭
print(pd.cut(ages, bisn, right=False))
# 设置面元的名称
names = ['青年', '年轻人', '中年人', '老年人']
print(pd.cut(ages, bisn, right=False, labels=names))

data1 = np.random.random(1000)
print(data1)
print(pd.cut(data1, 4, precision=2))

# 手动指定
cats = pd.cut(data1, [0, 0.1, 0.5, 0.9, 1])
print(cats)
print(pd.Series(cats).value_counts())

cats = pd.qcut(data1,[0, 0.1, 0.5, 0.9, 1])
print(pd.Series(cats).value_counts())