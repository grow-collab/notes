import pandas as pd

pd1 = pd.read_csv('数据/酒店评论信息.csv')
# print(pd1)
pd1.to_pickle('pickle_1')

pd2 = pd.read_pickle('pickle_1')
print(pd2)