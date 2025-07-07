import pandas as pd
import numpy as np

# Series 索引排序
ps = pd.Series(np.arange(5),index=list('DBACE'))
print(ps)
print(ps.sort_index()) # 升序 默认的
print(ps.sort_index(ascending=False)) # 降序


# DataFrame 索引排序
data = {
    'B':[82,65,49,23],
    'A': [80, 65, 89, 98],
    'D': [86, 66, 79, 27],
}
pf = pd.DataFrame(data,index=list('bcea'))
print(pf)
print(pf.sort_index()) # 跟行索引进行排序 默认
print(pf.sort_index(axis=1)) # 0代表行 1代表列