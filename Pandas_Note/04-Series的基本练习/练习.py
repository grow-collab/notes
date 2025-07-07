import pandas as pd

# 1.数据
data = {
    1:'龙仔',
    2:'麻辣龙虾',
    3:'小龙虾',
    4:None,
    5:'清蒸龙虾',
    6:'油焖大虾',
    7:'帝王虾',
    8:None,
    9:None
}

'''
1.按照上表创建Series(对象名"mydishes",索引名"dishes")
2.查看1-5的数据
3.查看那个索引的菜没有录入
4.获取7索引的菜
5.找出为帝王虾的菜品
'''
# 1.按照上表创建Series(对象名"mydishes",索引名"dishes")
ps = pd.Series(data)
ps.name = 'mydishes'
ps.index.name = 'dishes'
# print(ps.name)
# print(ps.index.name)

# 2.查看1-5的数据
print(ps)
print(ps[0:5]) # 包尾不包头
print(ps.head()) # head默认前5行

# 3.查看那个索引的菜没有录入
print(ps.isnull()) # 检查缺失值,如果为空,值为true,也就是没有录入的

# 4.获取7索引的菜
print(ps[7])

# 5.找出为帝王虾的菜品
print(ps == '帝王虾') # 使用运算符操作 算术运算符 比较运算符