import pandas as pd
import random

"""
1.根据上图创建一个DataFrame
2.对于创建的DataFrame进行转置
3.由于体育老师总是生病，成绩没有录入，所以删除该列数据
4.学校决定添加"历史"这个列，学生的这列的成绩分别是（25，87，45,34,65)
"""

# data2 = {
#     1:{'姓名':'张三','语文':random.randint(1,100),'数学':random.randint(1,100),'英语':random.randint(1,100),'体育':'0'},
#     2: {'姓名': '里斯', '语文': random.randint(1, 100), '数学': random.randint(1, 100), '英语': random.randint(1, 100),
#         '体育': '0'},
#     3: {'姓名': '小刘', '语文': random.randint(1, 100), '数学': random.randint(1, 100), '英语': random.randint(1, 100),
#         '体育': '0'},
#     4: {'姓名': '张了', '语文': random.randint(1, 100), '数学': random.randint(1, 100), '英语': random.randint(1, 100),
#         '体育': '0'},
#     5: {'姓名': '萨法', '语文': random.randint(1, 100), '数学': random.randint(1, 100), '英语': random.randint(1, 100),
#         '体育': '0'},
# }
data = {
    '姓名':['龙仔','麻辣龙虾','小炒虾','油焖大虾','帝王虾'],
    '语文':[54,43,56,59,22],
    '数学':[33,1,99,9,77],
    '英语':[72,93,35,16,36],
    '体育':[0,0,0,0,0]
}

# 1.根据上图创建一个DataFrame,两种数据创建方式都可以
pf = pd.DataFrame(data)
print(pf)

# 2.对于创建的DataFrame进行转置
pf2 = pf.T
print(pf2)

# 3.由于体育老师总是生病，成绩没有录入，所以删除该列数据
del pf['体育']
# print(pf)

# 4.学校决定添加"历史"这个列，学生的这列的成绩分别是（25，87，45,34,65)
pf['历史'] = [25,87,45,34,65]
print(pf)