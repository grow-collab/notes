val = '   x,v,D '

# 1.去除左右两边空格
# 列表推导式 语法结构:[表达式 for 变量 in 可迭代对象 if 条件]
p = [v.strip() for v in val.split(',')]
a, b, c = p
print(a, b, c)

# 2.字符串拼接
# 字符串加法
h = 'l' + ',' + 'l'
# 通过join
h1 = ','.join('lafaf')
print(h)
print(h1)

# 3.检查/检测
print('v' in val)

# 4.查找字符串
print(val.index('x'))  # index 返回的是 查找的第一个索引，一旦找不到就报错
print(val.find('d'))  # find 返回的是 查找到第一个索引，一旦找不到就返回-1

# 5.替换
print(val.replace('x','y'))

# 6.去除左/右空白字符
value1 = ' a'
value2 = 'p '
print(value1.lstrip())
print(value2.rstrip())

# 小写
print(val.lower())
# 大写
print(val.upper())

# 填充
print(val.ljust(11, '='))
print(len(val))
print(val.rjust(11, '='))
print(len(val))
