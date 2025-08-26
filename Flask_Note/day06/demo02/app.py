from flask import Flask, Response, request, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dfasfsdfhsdjklhfklsdjflksdjlfkdjsl'  # 加密密匙


@app.route('/')
def hello_world():
    return 'Hello World!'


# 设置cookie信息(存放在请求头里面) 原理 cookie(明文,不安全),session ==> token 浏览器的默认行为会带上发送到 后端
@app.route('/set_cookie/')
def set_cookie():
    response = Response('cookie设置')
    response.set_cookie('user_id', 'settings cookies')
    return response


# 获取cookie信息
@app.get('/get_cookie/')
def get_cookie():
    user_id = request.cookies.get('user_id')
    return f'获取的cookie是: {user_id}'


# 设置session(密文)
@app.route('/set_session/')
def set_session():
    session['username'] = 'zhangsan'
    return '设置成功'


@app.route('/get_session/')
def get_session():
    username = session.get('username')
    return f'session获取成功,{username}'


if __name__ == '__main__':
    app.run()

# mvt
