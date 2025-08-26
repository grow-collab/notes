import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# plt.ylabel('')
# plt.show()

# 三种接口
# 第一个接口
# plt.figure() # 画布
# plt.plot([1,2,3],[4,5,6])
# plt.show()

# 第二种接口的第一种方式
# fig,ax = plt.subplots() # 画布和区域
# ax.plot([1,2,3],[4,5,6])
# plt.show()

# 第二个接口的第二种方式
plt.rcParams['font.sans-serif'] = ['SimHei'] # 解决乱码问题
# fig = plt.figure() # 创造画布
# # 添加一个区域
# ax = fig.add_subplot()
# ax.plot(['北京','上海','广东'],[1,3,5])
# plt.show()

# 第二种接口的第三种方式
# fig = plt.figure() # 创建画布
# ax = plt.axes() # 添加画布
# ax.plot(['北京','上海','广东'],[1,3,5])
# plt.show()

# 第三种接口方式
import pylab
my_list = []
for content in range(10):
    my_list.append(content*2)
print(my_list)
pylab.plot(my_list)
pylab.show()

