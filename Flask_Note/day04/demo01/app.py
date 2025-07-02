from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from constants import DB_URI
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
db = SQLAlchemy(app)  # 获取数据库链接对象db
migrate = Migrate(app, db)  # 获取migrate对象


# 创建orm模型
# 创建user模型(一)
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False, default='123456')

    # 访问 User.articles


# 用户拓展信息
class UserExtension(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    identity = db.Column(db.String(18), default='111111222222')
    address = db.Column(db.String(120), nullable=True)
    # 外键绑定
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # 关系绑定 不能使用数组
    # uselist=False 代表反向引用的时候,不是一个列表,而是一个对象
    user = db.relationship('User', backref=db.backref('extension', uselist=False))


# 创建文章模型(多)
class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)
    # 外键 ==> 数据库层面的绑定
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # 表关系引用   relationship
    # backref 代表反向引用,代表User模型访问Article模型使用的字段
    author = db.relationship('User', backref='articles')

    # 访问 Article.author


# 映射数据库 数据迁移 Migrate
# 通过命令的方式映射数据库模型
#  与 git 命令非常相似
#  flask db init #初始化迁移文件
#  flask db migrate #将模型添加到迁移文件中
#  flask db upgrade将迁移文件映射到数据库中


@app.route('/')
def index():
    return '首页'


# 一对多关系映射
@app.route('/otm/')
def otm():
    user = User(username='凯尔', email='163@qq.com')
    article1 = Article(title='堕落天使', content='莫甘娜')
    article2 = Article(title='审判天使', content='天使彦')

    article1.author = user
    article2.author = user

    db.session.add_all([article1, article2])
    db.session.commit()

    return '一对多模型添加完成'


# 一对一映射
@app.route('/oto/')
def oto():
    user = User(username='卡萨丁', email='999@qq.com', password='666666')
    extra = UserExtension(identity='1234567890', address='空中花园')

    user.extension = extra

    db.session.add(user)
    db.session.commit()

    return '一对一模型添加完成'


if __name__ == '__main__':
    app.run()
