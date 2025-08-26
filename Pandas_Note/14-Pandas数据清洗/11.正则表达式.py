import re

string = 'hello 123 world 456'
# 创建正则表达式
pattern = r'\d+' # 匹配一个或多个数字

# 1.match 匹配开始位置,没有匹配成功返回一个空对象
result1 = re.match(pattern,string)
print(result1)

# 2.search 匹配整个字符串，返回第一个匹配成功的结果
result2 = re.search(pattern,string).group()
print(result2)

# 3.findall 匹配整个字符串，并返回匹配到的所有结果
result3 = re.findall(pattern,string)
print(result3)

# 4.split 分割
result4 = re.split(pattern,string)
print(result4)

# 5.sub 替换
result5 = re.sub(pattern,'llp',string)
print(result5)

str1 = '2025-7-3'
pattern1 = r'(\d+)-(\d+)-(\d+)'
result6 = re.match(pattern1,str1)
print(result6.group())
print(result6.group(1))
print(result6.group(2))
print(result6.group(3))
