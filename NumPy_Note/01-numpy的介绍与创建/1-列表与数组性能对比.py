import time
import numpy as np

# 性能对比
# 列表
start_time = time.time()
a = []
for x in range(100000):
    a.append(x ** 2)
end_time = time.time()
print("%.6f" % float(end_time - start_time))  # 0.011967897415161133

# 数组
start_time = time.time()
a = np.arange(100000) ** 2
end_time = time.time()
print("%.6f" % float(end_time - start_time))

#   终端输入 'jupyter notebook'
#   http://localhost:8888/tree?token=7588c186d2622a9893ba14fdd583582f9ed42ec481df3bdb