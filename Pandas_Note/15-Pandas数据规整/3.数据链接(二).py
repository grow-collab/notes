import pandas as pd
import numpy as np

# # join 合并
# left2 = pd.DataFrame([[1., 2.], [3., 4.], [5., 6.]], index=['a', 'c', 'e'], columns=['语⽂', '数学'])
# right2 = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.], [13., 14.]], index=['b', 'c', 'd', 'a'],
#                       columns=['英语','综合'])
# print(left2)
# print(right2)
#
# print(pd.merge(left2, right2, how='outer', left_index=True, right_index=True))
#
# # join是按照索引进⾏合并 join不能有重叠的列的
# left2=pd.DataFrame([[1.,2.],[3.,4.],[5.,6.]],index=['a','c','e'],columns=['语⽂','数学'])
# right2=pd.DataFrame([[7.,8.],[9.,10.],[11.,12.],[13,14]],index=['b','c','d','e'],columns=(['语⽂','综合'])
# left2.join(right2,how="outer") # 报错

# concat
arr1 = np.random.randint(0, 10, (3, 4))
arr2 = np.random.randint(0, 10, (3, 4))
print(arr1)
print(arr2)
# 1. Numpy的concat
# 示例代码:
# 沿轴⽅向将多个对象合并到⼀起
# np.concatenate
print(np.concatenate([arr1, arr2]))
print(np.concatenate([arr1, arr2], axis=1))

# 2. pd.concat
# 2.1. 注意指定轴⽅向，默认axis=0
# 2.2. join指定合并⽅式，默认为outer
# 2.3. Series合并时查看⾏索引有⽆重复
df1 = pd.DataFrame(np.arange(6).reshape(3, 2), index=list('abc'), columns=['one', 'two'])
df2 = pd.DataFrame(np.arange(4).reshape(2, 2) + 5, index=list('ac'), columns=['three', 'four'])
print(df1)
print(df2)
pd.concat([df1, df2])  # 默认外连接，axis-0
pd.concat([df1, df2], axis=1)  # 指定ax1s-1连接
# 同样我们也可以指定连接的⽅式为1nner
pd.concat([df1, df2], axis=1, join="inner")
