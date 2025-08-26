from http.client import HTTPException

from fastapi import APIRouter, Request
from models import *
from pydantic import BaseModel, validator
from fastapi.templating import Jinja2Templates
from typing import List
from fastapi.exceptions import HTTPException

student_router = APIRouter()


@student_router.get('/')
async def get_all_student():
    # (1) 查询所有 all方法
    # 在tortoise-orm下面,做数据库操作,必须异步支持
    # students = await Student.all() # Queryset: [Student(),Student(),Student()]
    # print('students:', students)

    # (2) 过滤查询 filter
    # students = await Student.filter(name='耿佳帅') # Queryset: [Student(),Student(),Student()]
    # students = await Student.filter(id=4) # Queryset: [Student(),Student(),Student()]
    # print('students', students[0].name)

    # (3) 过滤查询 get方法:返回模型类型对象
    # stu = await Student.filter(id=3)  # [Student(),]
    # stu = await Student.get(id=3)  # Student()
    # print(stu.name)

    # (4) 模糊查询
    # students = await Student.filter(sno__gt=113683)  # sno:字段,__gt=:大于
    # students = await Student.filter(sno__range=[1,113683])
    # students = await Student.filter(sno__in=[1,113683])
    # print(students)  # [<Student: 1>, <Student: 3>]

    # (5) values查询
    # students = await Student.filter(sno__range=[1,113683]) # [Student(),Student(),Student()]
    # students = await Student.all().values('name', 'sno')  # [{},{},{}...]
    # print(students)

    # (6) 一对多查询 多对多查询
    dd = await Student.get(name='彭于晏')
    print(dd.name)
    print(dd.sno)
    # print(dd.Clas_id)
    print(await dd.Clas.values('name'))  # {'name': '计算机科学与技术1班'}

    students = await Student.all().values('name', 'sno', 'Clas__name')

    print(await dd.course.all().values('name', 'teacher__name', 'addr'))

    students = await Student.all().values('name', 'sno', 'Clas__name', 'course__name')

    return {
        'info': students
    }


@student_router.get('/index.html')
async def get_template(request: Request):
    # ORM响应页面数据
    template = Jinja2Templates(directory='templates')

    students = await Student.all()
    return template.TemplateResponse('index.html', {
        'request': request,
        'students': students
    })


@student_router.get('/{student_id}')
async def get_one_student(student_id: int):
    student = await Student.get(id=student_id)
    return student


# 数据校验模型(请求)
class StudentIn(BaseModel):
    name: str
    sno: int
    pwd: str
    Clas_id: int
    course: List[int] = []

    @validator('name')
    def check_name(cls, value):
        assert value.isalpha(), 'name must be alpha'
        return value

    @validator('sno')
    def check_sno(cls, value):
        assert value > 1000 and value < 10000, 'sno must be between 1000 and 10000'
        return value


@student_router.post('/')
async def add_student(student_in: StudentIn):
    """
        添加新学生到数据库
        接收经过StudentIn验证的请求数据，执行数据库插入操作
        并返回创建的学生信息
    """
    # 数据库插入操作(两种常用方式)
    # 方式1：先实例化模型对象,再调用save()方法保存
    # student = Student(name=student_in.name, sno=student_in.sno, pwd=student_in.pwd, Clas=student_in.Clas) # 实例化,并传参
    # await student.save() # 插入到数据库student表

    # 方式2：直接使用模型的create()方法(推荐)
    student = await Student.create(name=student_in.name, sno=student_in.sno, pwd=student_in.pwd,
                                   Clas_id=student_in.Clas_id)

    # 多对多关系绑定
    choose_course = await Course.filter(id__in=student_in.course)
    # await student.course.clear()
    await student.course.add(*choose_course)

    return {
        'info': student
    }


@student_router.put('/{student_id}')
async def update_student(student_id: int, student_in: StudentIn):
    # 更改
    data = student_in.dict()
    print('data', data)
    course = data.pop('course')

    await Student.filter(id=student_id).update(**data)

    # 设置多对多的选修课程
    edit_stu = await Student.get(id=student_id)
    choose_course = await Course.filter(id__in=course)
    await edit_stu.course.clear()
    await edit_stu.course.add(*choose_course)

    return edit_stu


@student_router.delete('/{student_id}')
async def delete_student(student_id: int):
    # 删除
    delete_count = await Student.filter(id=student_id).delete()
    if not delete_count:
        raise HTTPException(status_code=404, detail='Student not found')

    return {
        'info': f'删除id为{student_id}的学生'
    }
