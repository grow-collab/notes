# 做用户的路由与视图
from flask import Blueprint, render_template

# 第一个参数为蓝图名称,用来区分不同的模块
# url_prefix 路由前缀
bp = Blueprint('user', __name__, url_prefix='/user/')


@bp.route('/login/')  # /user/login    × ==> /login
def login():
    return render_template('login.html')


@bp.route('/profile/')
def profile():
    return '个人中心页面'

# 总结 在蓝图里面做url反解析的时候,需要带上蓝图的名称
# 大家 下去 每一个知识点 敲一遍  优雅的代码 M V T ==> M V C
