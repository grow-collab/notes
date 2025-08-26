from tortoise.models import Model
from tortoise import fields


# 环境安装
# pip install tortoise-orm,aiomysql

# 选课系统
# 学生数据模型
class Student(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255, description='学生姓名')
    sno = fields.IntField(description='学号')
    pwd = fields.CharField(max_length=255, description='密码')

    # 一对多关系,班级与学生对应关系
    Clas = fields.ForeignKeyField('models.Clas', related_name='students')

    # 多对多关系,学生与课程对应关系
    course = fields.ManyToManyField('models.Course', related_name='students')


# 课程数据模型
class Course(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255, description='课程名称')
    teacher = fields.ForeignKeyField('models.Teacher', related_name='courses')
    addr = fields.CharField(max_length=32, description='教室', default='')


# 班级数据模型
class Clas(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255, description='班级名称')


# 教师数据模型
class Teacher(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255, description='教师名称')
    tno = fields.IntField(description='账号')
    pwd = fields.CharField(max_length=255, description='密码')
