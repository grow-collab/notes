import pandas as pd
import numpy as np

'''
方法                          描述
add,radd                    加法 （+)
sub,rsub                    减法（-)
div,rdiv                    除法（/）
floordiv, rfllordiv         整除（//）
mul，rmull                  乘法（*）
pow，rpow                   幂次⽅（**）
字⺟r开头 会翻转参数
'''

# Series 算术方法
ps1 = pd.Series(np.arange(9), index=['a', 'b', 'c', 'd', 'f', 'e', 'g', 'l', 'p'])
# print(ps1)
ps2 = pd.Series(np.arange(6), index=['a', 'b', 'c', 'd', 'f', 'e'])
# print(ps2)
# print(ps1+ps2)
# fill_value,将缺失值设置为0
# print(ps1.add(ps2,fill_value=0))


# DataFrame 算术方法
pf1 = pd.DataFrame(np.arange(9).reshape(3, 3), index=['a', 'b', 'c'], columns=['A', 'B', 'C'])
pf2 = pd.DataFrame(np.arange(12).reshape(3, 4), index=['a', 'b', 'c'], columns=['A', 'B', 'C', 'D'])
print(pf1)
print(pf2)
print(pf1.add(pf2, fill_value=0))

print(pf1.reindex(columns=pf2.columns, fill_value=0))

# 字⺟r开头 会翻转参数
pf3 = pd.DataFrame(np.arange(3).reshape(1, 3), index=['a'], columns=['A', 'B', 'C'])
pf4 = pd.DataFrame(np.arange(4, 7).reshape(1, 3), index=['a'], columns=['A', 'B', 'C'])
print(pf3)
print(pf4)
# print(pf3.sub(pf4))
print(pf3.rsub(pf4))  # 减与被减调换位置
