import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(12).reshape(3, 4), index=['a', 'b', 'c'], columns=['one', 'two', 'three', 'four'])
# print(df)

print(df.reindex(['a', 'c', 'b']))
# 利用重写索引 改成ABC还能不能呢/
print(df.reindex(['A', 'B', 'C']))
# 没有发现没有任何数据 这是需要注意的 其次 reindex返回的是一个新对象
# 不会对源数据进行修改

# 1.使用重命名轴索引
tran = lambda x: x[:4].upper()
# print(df.index.map(tran))
df.index = df.index.map(tran)
print(df)  # 修改源数据的情况下

# 2.不修改源数据 rename
# 字符串方法中 title所表示的意思是 将每一个单词的首字母转换为大写
df1 = pd.DataFrame(np.arange(12).reshape(3, 4), index=['add', 'bdd', 'cdd'], columns=['one', 'two', 'three', 'four'])
print(df1.rename(index=str.title, columns=str.upper))

# 3.自定义 结合字典做一个映射
df1.rename(index={'add': 'Yi', 'bdd': 'Er', 'cdd': 'Thr'},
                columns={'one': 'O', 'two': 'T', 'three': 'E', 'four': 'F'},inplace=True)
print(df1)
