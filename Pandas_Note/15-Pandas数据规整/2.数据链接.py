import pandas as pd
import numpy as np

left = pd.DataFrame({'key': ['KO', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['KO', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})
print(left)
print(right)
# 数据链接
# pd.merge
# 根据当个或者多个健将不同DataFrame的⾏链接起来
# 类似数据库的链接操作
'''
pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=True,
         suffixes=('_x', '_y'), copy=True, indicator=False)
         
参数介绍:        
1.left和right：两个不同的DataFrame；
    左链接left:对所有左表的健进⾏联合
    右链接right:对两张表都有的健的交集进⾏联合
    outer:全链接：对两者表的都有的健的并集进⾏联合
2.how：连接⽅式，有inner、left、right、outer，默认为inner；
    内链接inner 对两张表都有的健的交集进⾏联合
3.on：指的是⽤于连接的列索引名称，必须存在于左右两个DataFrame中，如果没有指定且其他参数也没有指定，则以两个DataFrame列名交集作为连接键；
4.left_on：左侧DataFrame中⽤于连接键的列名，这个参数左右列名不同但代表的含义相同时⾮常的有⽤；
5.right_on：右侧DataFrame中⽤于连接键的列名；
6.left_index：使⽤左侧DataFrame中的⾏索引作为连接键；
7.right_index：使⽤右侧DataFrame中的⾏索引作为连接键；
8.sort：默认为True，将合并的数据进⾏排序，设置为False可以提⾼性能；
9.suffixes：字符串值组成的元组，⽤于指定当左右DataFrame存在相同列名时在列名后⾯附加的后缀名称，默认为('_x', '_y')；
10.copy：默认为True，总是将数据复制到数据结构中，设置为False可以提⾼性能；
11.indicator：显示合并数据中数据的来源情况
'''
print(pd.merge(left, right))
