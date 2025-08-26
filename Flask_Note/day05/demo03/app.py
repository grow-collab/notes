from flask import Flask, render_template, request, redirect, url_for, jsonify
from forms import LoginForm, RegisterForm

app = Flask(__name__)


# flask-wtf 验证用户提交数据的合法性
# 安装 pip install  flask-wtf #表单校验
# 安装 pip install email_validator #邮箱校验

@app.route('/')
def hello_world():
    return '首页'


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        # 表单校验,获取到校验的结果(true/false)
        print('表单的邮箱地址: ', request.form.get('email'))
        form = LoginForm(request.form)
        if form.validate():
            return '登录成功!'
        else:
            return '表单校验失败'
            # return redirect(url_for('login'), err='错误信息')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        print('注册表单参数: ', request.form.get('name'))
        form = RegisterForm(request.form)
        if form.validate():
            return '表单校验成功!'
        else:
            return '表单校验失败!'


@app.route('/index/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        # 拿到前端传递过来的值
        name = request.values.get('name')
        password = request.values.get('password')
        # 做一些操作
        # 给前端返回响应的状态信息
        return jsonify({
            'code': 200,
            'message': '登录成功!',
            'name': name,
            'password': password
        })


if __name__ == '__main__':
    app.run()

# 表单参数的传递

# 综合大项目==>个人网站==>部署到服务器
