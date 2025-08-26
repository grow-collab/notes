import pandas as pd

# ⽤于从 Excel ⽂件中读取数据并将其加载到 pandas 的 DataFrame 中。
pd1 = pd.read_excel('数据/酒店评论信息.xlsx')
print(pd1)