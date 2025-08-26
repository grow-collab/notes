import pandas as pd

# 1.创建字典数据
# key:value  键值对
data = {
    '姓名':['张三','李四','小白','小红'],
    '年龄':[20,18,21,23],
    '性别':['男','男','男','女']
}

# 2.创建一个DataFrame对象
pf = pd.DataFrame(data)

# 3.输出
print(pf)

'''
   姓名  年龄 性别
0  张三  20  男
1  李四  18  男
2  小白  21  男
3  小红  23  女
这里的0 1 2 3 是索引/下标，类似于列表
'''
# 4.写入到Excel表格当中
# to_excel('文件的地址+文件名',index=True),index 默认开启
pf.to_excel('./excel.xlsx',index=False)
pf.set_index('姓名',inplace=True)# 设置下标,将姓名设置为下标
# inplace在当前文件中修改
# False 重新建一个文件,覆盖当前文件