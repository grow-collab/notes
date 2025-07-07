import pandas as pd
import numpy as np

# Series 值排序
ps = pd.Series([65,49,89,95,61],index=list('DBACE'))
print(ps)
print(ps.sort_values()) # 升序 默认的
print(ps.sort_values(ascending=False)) # 降序


# DataFrame 值排序
data = {
    'B':[82,65,49,23],
    'A': [80, 65, 89, 98],
    'D': [86, 66, 79, 27],
}
pf = pd.DataFrame(data,index=list('bcea'))
print(pf)
print(pf.sort_values(by='B',axis=0))
print(pf.sort_values(by='a',axis=1,ascending=False))
# by 设置行索引 axis = 1
# by 设置列索引 axis = 0
print(pf.sort_values(by=['B', 'D', 'A'],ascending=False))
# 优先级 现根据B进行排序 B列中有相同的数据 就根据D列中数据进行排序
