import pandas as pd
import numpy as np

# 混合运算
pf1 = pd.DataFrame(np.arange(9).reshape(3,3),index=['a','b','c'],columns=['A','B','C'])
pf2 = pd.DataFrame(np.arange(12).reshape(3,4),index=['a','b','c'],columns=['A','B','C','D'])
print(pf1)
# print(pf2)

ps = pf1.loc['a'] # 通过高级索引取行
# print(ps)
# print(pf1 - ps) # 每一行都要减ps的值

ps2 = pf1['A'] # 取列
print(ps2)
print(pf1.sub(ps2,axis=0)) # 每一列减ps2