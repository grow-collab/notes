import pandas as pd
import numpy as np

# Series
# a.增加
ps = pd.Series(np.arange(5),index=['a','b','c','d','e'])
print(ps)
ps['f'] = 7
print(ps) # 在原有的基础上增加

# 怎么在不修改原有数据的基础上添加呢
s = pd.Series({'g':9})
ps2 = ps._append(s)
print(ps2)


# DataFrame
# a.增加
pf = pd.DataFrame(np.arange(9).reshape(3,3),index=['a','b','c'],columns=['A','B','C'])
print(pf)

# 增加列
pf[4] = 9 # 这⾥所表示的 增加是⼀列 默认的 数据全是9
# 不想让数据⼀模⼀样
pf[4] = [9,12,31] # 增加是⼀列 数据9 12 31
print(pf)

# 插入操作 insert(插⼊的位置,插⼊的索引,插⼊的数据)
pf.insert(0,'k',[1,2,3]) # loc must be int
print(pf)

# 增加行
# 标签索引 loc
pf.loc['d'] = [9,6,5,1,7]
print(pf)

row = {'E':1,'c':6}
# pf1 = pf._append(row)
# print(pf) # 报错要忽略

pf1 =  pf._append(row,ignore_index=True)
print(pf1)