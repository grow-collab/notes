import pandas as pd
import numpy as np

# Series 算术运算和数据对齐
ps1 = pd.Series(np.arange(9),index=['a','b','c','d','f','e','g','l','p'])
# print(ps1)
ps2 = pd.Series(np.arange(6),index=['a','b','c','d','f','e'])
# print(ps2)

# 算术运算符 加减乘除(+-*/) 取余%
ps3 = ps1+ps2
# print(ps3)


# DataFrame 算术运算和数据对齐
pf1 = pd.DataFrame(np.arange(9).reshape(3,3),index=['a','b','c'],columns=['A','B','C'])
pf2 = pd.DataFrame(np.arange(12).reshape(3,4),index=['a','b','c'],columns=['A','B','C','D'])
print(pf1)
print(pf2)
print(pf1+pf2)
# print(pf1*pf2)
