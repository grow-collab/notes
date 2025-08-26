import pandas as pd
import numpy as np

data = {
    '小红':'13658213@qq.com',
    '小白':'1596431596@qq.com',
    '小黑':'51325986@gmail.com',
    '绿绿':np.nan
}
ps = pd.Series(data)
print(ps)
print(ps.isnull())

print(ps.map(lambda x:str(x).split('@')))

# 是否包含qq
# print(ps.loc[ps.str.contains('qq')])
# 替换
print(ps.str.replace('qq', 'gmail'))
# 分割
print(ps.str.split('@'))
# 提取第一个元素
print(ps.str.get(0))
# 截取
print(ps.str.slice(0, 3))
# 正则 返回的是一个DataFrame对象
print(ps.str.extract(r'(\d+)'))
# 查找
print(ps.str.findall('@'))
# 切割
print(ps.str[:5])
