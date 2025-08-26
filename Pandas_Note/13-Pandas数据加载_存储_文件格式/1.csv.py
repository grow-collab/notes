import pandas as pd
'''
相对路径:从自身出发
绝对路径:从根本出发

例子:龙仔现在在哪里
中国/湖北/武汉/江夏区/龙仔的公司/直播间 绝对路径

直播间/  相对路径

文件
D:\项目\数据分析\Pandas\\13-Pandas数据加载_存储_文件格式\数据\酒店评论信息.csv 绝对路径
/数据/酒店评论信息.csv                                       相对路径
'''
# read_csv:从⽂件、URL、⽂件型对象中加载带分隔符的数据，默认分隔符为逗号
# 1.header=None 使用默认列名,也可以通过names设置⾃定义的列名
pd1 = pd.read_csv('./数据/酒店评论信息.csv',header=None,names=['A','B','C','D','E'])
print(pd1)

# 2.在⼀些特殊情况下 需要将某⼀列变成⾏索引 可以通过参数 index_col进⾏设置
pd2 = pd.read_csv('./数据/酒店评论信息.csv',header=None,names=['A','B','C','D','E'],index_col='A')
print(pd2)

# 3.设置层级索引
pd3 = pd.read_csv('数据/酒店评论信息.csv',header=None,names=['A','B','C','D','E'],index_col=['A','B'])
print(pd3)