from flask import Flask, g, render_template

app = Flask(__name__)


# 上下文(全局对象)
# 应用上下文 : g 登录状态保持(cookie信息)
# 全局上下文 : request (获取表单的值) response session(保持一些会话信息)


# 钩子函数(在某一件事情执行前后执行的函数) ==> 回调函数(等待某一件事情完成之后的函数)

# 第一次请求之前执行的钩子函数,只会执行一次,在 Flask 2.3 及之后的版本中，before_first_request 装饰器被移除了
@app.before_first_request
def first_request():
    print('处理第一次请求之前!')


# 每次请求之前执行的钩子函数,做一个登录状态保持
@app.before_request
def before_request():
    if not hasattr(g, 'user'):
        setattr(g, 'user', '萧兮')

    print('每次请求的钩子函数')


# 每次请求之后执行的钩子函数
@app.teardown_appcontext
def teardown(exc=None):
    print('请求之后的回调函数')


# 错误处理的钩子函数
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.route('/index/')
def index():
    return 'index'


@app.route('/')
def home():
    return 'home'


@app.route('/user/')
def user():
    return f'user, {g.user}'


if __name__ == '__main__':
    app.run()

# 总结一下 :钩子函数的执行顺序
# 当一个请求来得时候 ==> before_first_request ==> before_request ==> 视图函数 ==> 视图函数中返回的模板 ==> teardown_appcontext


# ajax  ==> 菜鸟教程

# 数据交互:

# 1.原生js
# 2.jquery的ajax
# 3.fetch
# 4.axios

