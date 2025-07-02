# 蓝图文件
from flask import Blueprint
from ext import db
from models import User

bp = Blueprint('inedx', __name__, url_prefix='/')


# 映射模型
@bp.route('/')
def hello_world():
    return '首页路由地址'


# 添加操作
@bp.route('/add/')
def add():
    one_user = User(username='海绵宝宝', email='169@qq.com')
    two_user = User(username='派大星', email='666@qq.com')
    three_user = User(username='蟹老板', email='888@qq.com')

    db.session.add_all([one_user, two_user, three_user])
    db.session.commit()
    return '添加数据成功!'


# @bp.route('/add/', methods=['GET', 'POST'])
# def add():
#     if request.method == 'GET':
#         return render_template('add.html')
#     else:
#         try:
#             username = request.form.get('username')
#
#             one_user = User(username=username, email='169@qq.com')
#             two_user = User(username='派大星', email='666@qq.com')
#             three_user = User(username='蟹老板', email='888@qq.com')
#
#             db.session.add_all([one_user, two_user, three_user])
#             db.session.commit()
#             return jsonify({
#                 'code': 200,
#                 'message': '数据添加成功!'
#             })
#         except Exception as e:
#             print('错误信息: ', e)
#             return jsonify({
#                 'code': 500,
#                 'message': '数据添加失败!'
#             })


# 查询操作
@bp.route('/search/')
def search():
    # session.query(User).filter
    user = db.session.query(User).filter_by(username='海绵宝宝').first()
    print(user.email)
    return '查询成功!'


# 修改操作
@bp.route('/update/')
def update():
    user = User.query.filter_by(username='海绵宝宝').first()
    user.password = '999999'
    db.session.commit()
    return '修改成功!'


# 删除操作
@bp.route('/delete/')
def delete():
    try:
        user = db.session.query(User).filter_by(username='海绵宝宝').first()
        db.session.delete(user)
        db.session.commit()
    except Exception as e:
        print(e)
    return '删除相关方法'
