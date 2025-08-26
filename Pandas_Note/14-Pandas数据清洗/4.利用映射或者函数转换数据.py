import pandas as pd

df = pd.DataFrame({'food': ['Apple', 'orange', 'banana', 'Mango', 'apple', 'motato'],
                     'price': [19.9, 12, 16, 20, 30, 1.2]})

print(df)
# 1.先建⽴⼀个对应关系
meta = {
    'Apple': 'fruit',# 这个⽅式标记麻烦
    'orange': 'fruit',
    'banana': 'fruit',
    'mango': 'fruit',# 转⼩写记得改
    'apple': 'fruit',
    'motato': 'vegetable'
}

# 2.通过字符串的操作转换成小写
low = df['food'].str.lower()
# print(low)
df['food'] = low

# 3.这个map可以接受⼀个函数 或者是含有对应关系(映射关系的对象)
# map()可以接受⼀个映射函数或字典,来映射转换Series中的每个值:
# print(df['food'].map(meta))
df['type'] = df['food'].map(meta)
# print(df)

# 函数 利用匿名函数 lambda
df['class'] = df['food'].map(lambda x:meta[x.lower()])
print(df)

# 对每⾏应⽤求和函数
print(df.apply(lambda x: x.sum(), axis=1))
# 最⼤
print(df.apply(lambda x: x.max(), axis=1))
# 最⼩
print(df.apply(lambda x: x.min(), axis=1))
# 求平⽅
print(df.apply(lambda x: x.pow(2), axis=1))
# 求绝对值
print(df.apply(lambda x: x.abs(), axis=1))
# 四舍五⼊
print(df.apply(lambda x: x.round(), axis=1))
'''
apply()会遍历Series/DataFrame,并将每⼀元素/⾏/列传给函数执⾏。可以通过axis参数控制
是逐列还是逐⾏应⽤。
map()/apply()提供了在pandas中灵活转换数据的⽅式。需要对数据集抽象执⾏操作时可以活⽤它
们。
'''