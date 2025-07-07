import pandas as pd

'''
read_clipboard()
它可以从剪贴板读取数据，并将其加载到 pandas 的 DataFrame 中

使⽤ pd.read_clipboard() 的步骤如下： 
1. 复制要读取的数据到剪贴板（可以是表格形式的数据）。
2. 运⾏ pd.read_clipboard() 代码。
请注意，pd.read_clipboard() 函数依赖于剪贴板中的数据的格式正确性。确保复制的数据在表格中是对⻬
的，并且在运⾏代码之前没有对剪贴板进⾏其他操作。
'''
pd1 = pd.read_clipboard()
print(pd1)