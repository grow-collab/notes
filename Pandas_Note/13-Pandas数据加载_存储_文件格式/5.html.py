import pandas as pd

# 读取HTML⽂档中的所有表格
pd1 = pd.read_html('https://www.dxsbb.com/news/131783.html',encoding='gbk')
print(pd1)