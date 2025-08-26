import pandas as pd
import numpy as np

# Series
# b.删除
ps = pd.Series(np.arange(5),index=['a','b','c','d','e'])
print(ps)

# del
del ps['b'] # 这种方式不推荐 在原有对象上修改
print(ps)

# drop 删除轴上数据
ps1 = ps.drop('e') # 不会在原有的对象上进⾏修改 是创建⼀个新的对象 并删除 返回
print(ps)
print(ps1)

ps2 = ps.drop(['a','e']) # 删除多行数据
print(ps2)


# DataFrame
# b.删除
pf = pd.DataFrame(np.arange(9).reshape(3,3),index=['a','b','c'],columns=['A','B','C'])
print(pf)

# del
# 删除列
del pf['A']
print(pf)

# 删除行
pf1 = pf.drop('a') # 删除单行
print(pf1)
pf2 = pf.drop(['a','c']) # 多行
print(pf2)

# 指定删除列 drop(索引,轴=0)
# pf3 = pf.drop('B',axis=1) # 1是列 0是⾏ 默认为0
pf3 = pf.drop('B',axis='columns') # 等同于上⾯的效果
print(pf3)

print(pf)
# drop 的 inplace属性 是否在原对象删除 默认为False
pf.drop('C',axis=1,inplace=True)
print(pf)