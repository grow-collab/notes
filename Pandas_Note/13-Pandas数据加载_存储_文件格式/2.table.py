import pandas as pd

# read_table:从⽂件、URL、⽂件型对象中加载带分隔符的数据，默认分隔符为制表符（"\t"）
pd1 = pd.read_table('数据/例子1.txt')
print(pd1)