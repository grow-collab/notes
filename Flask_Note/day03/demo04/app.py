from flask import Flask
import user

app = Flask(__name__)
# 蓝图 模块化拆分
# 注册蓝图
app.register_blueprint(user.bp)


@app.route('/')
def hello_world():
    return 'app首页'


if __name__ == '__main__':
    app.run()
