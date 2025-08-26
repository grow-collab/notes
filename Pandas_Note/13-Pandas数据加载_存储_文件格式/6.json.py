import json
import pandas as pd

'''
1.什么是json
javaScript Object Notation
'''
# with open('数据/测试.json',mode='r',encoding='utf-8') as f:
#     file = f.read()
#     print(type(file))
#     file2 = json.loads(file)
#     print(type(file2))

obj = '{"queryExt": "⼩姐姐","listNum": 1974}'
# 将json数据转换成python对象
res = json.loads(obj)
print(res)
print(type(res))
# python对象转换成json数据
res1 = json.dumps(res)
print(res1)
print(type(res1))
print(res['queryExt'])
pd1 = pd.DataFrame(res,columns=['queryExt','listNum'],index=[1,0])
print(pd1)
