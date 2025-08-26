from flask import Flask, url_for, request, redirect

app = Flask(__name__)


# 构造url ==> url_for

# @app.route('/')
# def home():
#     print(url_for('article', id=999, key='cat', age=18))  # /article/999?key=cat
#     return '首页'
#
#
# @app.route('/article/<id>')
# def article(id):
#     return '文章列表页: ' + id


# @app.route('/')
# def home():
#     print(url_for('article'))
#     return '首页'
#
#
# @app.route('/article/')
# def article():
#     return '文章列表页'


# url末尾的 / 斜线
# 请求 /article 的时候 会自动跳转(重定向)到/article/
#
# 后端渲染 ==> 快 , 利于seo优化排名
# https://car.autohome.com.cn/price/brand-15.html/  .aspx  .jsp ==> (后端渲染)
# 老项目

# @app.route('/article/')
# def article():
#     return '文章列表页'


# 指定 http 请求方法 ==> [get post put delete]
# 在地址栏上发起的请求都是get请求
#
# @app.route('/article/', methods=['POST'])
# def article():
#     return '文章列表页'


# 页面跳转(重定向) redirect
# 登录 /login

@app.route('/logindsadasda/', methods=['GET'])
def login():
    return '登录页面'


@app.route('/user/', methods=['GET'])
def user():
    name = request.args.get('name')

    if not name:
        return redirect(url_for('login'))
    else:
        return f'欢迎您,{name}'


if __name__ == '__main__':
    app.run()
