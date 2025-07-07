import numpy as np
import pandas as pd

# Series
ps = pd.Series(['a','b','c',np.NaN,'d'])
# print(ps)
# isnull:判断是否存在缺失值,有缺失值的位置就返回True
# notnull:与上面的isnull相反
ps[0] = None
print(ps.isnull()) # 返回的是一个Series对象 bool
# print(ps.notnull())

# 过滤/滤除缺失值
print(ps.dropna())
# 将缺失值设置为指定的数值
print(ps.fillna(1))