import pandas as pd
import numpy as np

# Series
ps = pd.Series([1,2,3,np.nan,5,np.nan])
print(ps)
# isnull 判断是否存在缺失值
print(ps.isnull())
# 丢弃缺失值
print(ps.dropna())
# 将缺失值设置为指定的数值
print(ps.fillna(0))


# DataFrame
data = {
    'A':[1,5,9,6],
    'B':[np.nan,5,8,3],
    'C':[7,4,np.nan,np.nan]
}
pf = pd.DataFrame(data)
print(pf)
# 判断是否存在缺失值
print(pf.isnull())
# 丢弃缺失值
print(pf.dropna()) # 默认丢弃行
print(pf.dropna(axis=1)) # axis=1 通过axis调整,为1则丢失列
# 将缺失值设置为指定值
print(pf.fillna(0))