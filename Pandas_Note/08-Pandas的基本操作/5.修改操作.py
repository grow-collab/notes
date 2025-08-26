import pandas as pd
import numpy as np

# Series
# c.修改
ps = pd.Series(np.arange(6),index=['a','b','c','d','e','f'])
print(ps)

ps['d'] = 6 # 直接通过索引修改
print(ps)


# DataFrame
# c.修改
pf = pd.DataFrame(np.arange(9).reshape(3,3),index=['a','b','c'],columns=['A','B','C'])
print(pf)

# 根据列进行修改
pf['A'] = 9
print(pf)
pf['A'] = [9,5,6] # 多值
print(pf)

# 不太常⻅ 对象.列 ⽅式
pf.A = [6,5,7]
print(pf)

#loc 标签索引 ⾏索引修改
pf.loc['a'] = [9,7,3]
print(pf)

# 指定位置实现
pf.loc['b','C'] = 0
print(pf)