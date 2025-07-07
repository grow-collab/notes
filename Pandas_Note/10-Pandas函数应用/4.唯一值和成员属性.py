import pandas as pd

# Series
ps = pd.Series([1,1,9,6,5,5])
print(ps)
# 通过unique() 返回一组唯一值的数组
pu = ps.unique()
print(pu)
print(type(pu))
# is_unique 判断Series中的值是不是唯一的布尔
print(ps.is_unique)
# 计数
print(ps.value_counts()) # 返回一个Series

# 成员属性 判断值是否存在
print(ps.isin([9,6])) # 返回一个Series 布尔


# DataFrame
data = {
    'A':[3,7,9,5],
    'B': [8,9,5,2],
    'C': [6,9,4,1],
}
pf = pd.DataFrame(data)
print(pf)
# print(pf.isin([8, 5]))
print(pf.value_counts())