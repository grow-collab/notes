from flask import Flask, render_template, request, jsonify
from flask.views import MethodView

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


# 使用最多==>方便
@app.route('/')
def hello_world():
    return 'dasdas'


# 编写后端接口==> 方便 restfulAPI
# 类视图(基于调度方法==>请求方法)
class LoginView(MethodView):
    # 当客户端通过get请求进行访问的时候
    def get(self):
        return render_template('login.html')
        # return jsonify({
        #     'name': '张三',
        #     'age': 18
        # })

    # 当客户端通过post请求进行访问的时候
    def post(self):
        # 获取表单传递过来的值
        email = request.form.get('email')
        password = request.form.get('password')
        print(email, password)
        # 查询数据库,判断用户是否存在
        if email == 'admin@qq.com' and password == '123456':
            return '登录成功!'
        else:
            return '用户名或密码错误!'


# add_url_rule添加映射关系 as_view==> 反解析url_for('loginview') ==> /myuser/
app.add_url_rule('/myuser/', view_func=LoginView.as_view('loginview'))

if __name__ == '__main__':
    app.run()
