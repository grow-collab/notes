# 安装一下flask的包

# 从flask框架中导入Flask类
from flask import Flask

# 传入一个__name__初始化一个Flask实例
app = Flask(__name__)


# http://150.158.21.251:4000 /search ? keywords=海阔天空(加buff)

# python基础语法里面 装饰器 ( 路由 与 视图 的对应关系)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/search/')
def search():
    return 'search视图函数'


# 开启调试模式 # 热更新
# 修改host 端口号


if __name__ == '__main__':
    # 启动app实例,启动web服务
    app.run(host='0.0.0.0',port=9000)
