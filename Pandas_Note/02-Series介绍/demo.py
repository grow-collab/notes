import numpy
import pandas as pd

# 三种创建方式
# 1.列表方式
data = ['wo','ai','ni']
ps = pd.Series(data,index=['2','3','4'])
print(ps)

# 2.Numpy数组方式
arr = numpy.array([1,2,3])
s = pd.Series(arr,index=['2','3','i'])
print(s)

# 3.字典方式
dict = {
    '1':'wi',
    '2':'ni',
    '3':'ai'
}
# key 对应索引,value 对应element元素数据
s = pd.Series(dict,index=['0','1','2'])
print(s)

