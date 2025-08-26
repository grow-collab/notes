import pandas as pd
import numpy as np

pf = pd.DataFrame(np.random.randn(3,4))
print(pf)
# print(np.abs(pf)) # 取绝对值

# 1.通过apply将函数应用到列或行
u = lambda x:x.max()
print(pf.apply(u)) # 默认为列 axis=0

print(pf.apply(u, axis=1)) # 行


# 2.通过map 将函数应⽤到每个函数
# a = 0.2222
# print('%.2f' % a)
# print(pf.applymap(lambda x: '%.2f' % x)) # 注意applymap被弃用,直接使用map
print(pf.map(lambda x: '%.2f' % x))
