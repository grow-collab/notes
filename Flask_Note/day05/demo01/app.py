from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from constant import DB_URI

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)

# 一对多 ==> 高效

# 多对多
tb_student_course = db.Table(
    'tb_student_course',
    db.Column('student_id', db.Integer, db.ForeignKey('students.id')),
    db.Column('course_id', db.Integer, db.ForeignKey('courses.id'))
)


# 创建orm模型
class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)

    # 关联属性
    relate_courses = db.relationship('Course', secondary=tb_student_course, backref='relate_student')


# 选课模型
class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)


@app.route('/')
def hello_world():
    return '首页!'


@app.route('/mtm/')
def mtm():
    stu1 = Student(name='张三')
    stu2 = Student(name='李四')
    stu3 = Student(name='王五')

    cou1 = Course(name='物理')
    cou2 = Course(name='化学')
    cou3 = Course(name='生物')

    # 添加关系
    stu1.relate_courses = [cou2, cou3]
    stu2.relate_courses = [cou2]
    stu3.relate_courses = [cou1, cou2, cou3]

    db.session.add_all([stu1, stu2, stu3, cou1, cou2, cou3])
    db.session.commit()

    return '数据添加完成!'


if __name__ == '__main__':
    app.run()

# 项目重构
