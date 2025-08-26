import pandas as pd

# 准备数据
data = [1,2,3,4]
# 创建一个Series数据结构的对象
pS = pd.Series(data,index=['0','1','2','3'])

print(pS.values) # 获取值
print(pS.index) # 获取下标

# 检查缺失值
print(pS.isnull())
print(pS.notnull())

# 获取数据值(索引,切片,选择多个和loc方法等)
print(pS['0']) #  通过索引获取
print(pS['0':'3']) # 通过切片获取，包头包尾
print(pS[['0','2']]) # 选择多个
print(pS.loc['0']) # 通过loc方法获取a的value值


# name属性 添加名称(为对象命名)
pS.name = 'student' # 为对象命名
pS.index.name = 'student_index' # 为对象的索引命名

print(pS.name)
print(pS.index.name)


# 获取指定行数据
# 字典
# data = {
#     'a':2,
#     'b':3,
#     'c':4
# }

data = ['1','2','3','4','5','6'] # 列表

ps = pd.Series(data)

print(ps.head()) # 默认前5行
print(ps.tail(2)) # 默认后5行，后两行数据