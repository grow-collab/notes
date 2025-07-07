import numpy as np
import pandas as pd

data = pd.DataFrame(np.arange(5 * 4).reshape(5, 4))
print(data)
# 创建一个新的数组 0-4
sam = np.random.permutation(5)
print(sam)
# 排列
print(data.take(sam))

# 随机采样
print(data.sample(n=2))

ps = pd.Series([5, 7, 1, 6, 3])
print(ps)
print(ps.sample(n=10, replace=True))
