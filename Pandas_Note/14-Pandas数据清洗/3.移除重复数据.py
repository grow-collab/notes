import pandas as pd
import numpy as np

df = pd.DataFrame({'name': ['龙仔', '龙虾'] * 3 + ['胖达'],
                   'age': [18, 20, 18, 32, 23, 26, 20]}
                  )
print(df)
# duplocated: 返回的是一个Series对象
# 检查是否有重复数据行
# print(df.duplicated())

# 删除重复行的数据 drop_duplicates()
# print(df.drop_duplicates())

df['sex'] = ['男','女','男','女','男','女','女']
print(df)
# 默认保留第一次出现的数据 删除第二次出现的
print(df.drop_duplicates(['name'])) # 指定列
# 删除第一次出现的数据,保留最后一次出现的
print(df.drop_duplicates(['sex'], keep='last'))