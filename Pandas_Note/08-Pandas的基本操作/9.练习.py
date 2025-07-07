import pandas as pd
import numpy as np

'''
案例练习:
1.观察结构，调整列索引顺序为(id,学生id,学生姓名,年龄,性别,语文成绩,数学成绩,英语成绩,学生是否毕业,学生是否休学)
2.增加一列关于学生状态(可使用1代表 在 0代表不在)
3.删除id这一列
4.查找出学生语文成绩大于90分的并输出的时候只有学生id-语文成绩
'''
# 读取数据
students = pd.read_excel('student.xlsx')
# print(students)

# 1.观察结构，调整列索引顺序为(id,学生id,学生姓名,年龄,性别,语文成绩,数学成绩,英语成绩,学生是否毕业,学生是否休学)
students = students.reindex(columns=['id','学生id','学生姓名','年龄','性别','语文成绩','数学成绩','英语成绩','学生是否毕业','学生是否休学'])
print(students)

# 2.增加一列关于学生状态(可使用1代表 在 0代表不在)
# apply() ⽅法将会遍历 学⽣是否休学 列的每个值，并将条件逻辑应⽤到每个值上。
# 参数 x 代表的是每个元素值，也就是 学⽣是否休学 列中的每个值。
students['学生状态'] = students['学生是否休学'].apply(lambda x:0 if x == '是' else 1)
print(students)

# 3.删除id这一列
students = students.drop('id',axis=1) # 1是列 0是行 默认为0
print(students)

# 4.查找出学生语文成绩大于80分的并输出的时候只有学生id-语文成绩
students = students[students['语文成绩'] >= 80]
students = students.loc[:,'学生id':'语文成绩']
print(students)