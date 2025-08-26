from flask import Flask, jsonify
import config

app = Flask(__name__)

# 第一种方式: 直接编码
# app.config['JSON_AS_ASCII'] = False

# update方式
# app.config.update(
#     JSON_AS_ASCII=False,
#     key=value
# )

# 第三种方式 抽离config配置文件
# 写入配置
# app.config.from_object(config)


# pyfile方式==> 直接传入一个文件 .py .txt
# app.config.from_pyfile('config.py')


# 前后端通讯 返回的是json数据
@app.route('/api')
def hello_world():
    return jsonify({
        "name": 'flask',
        "message": '快速,轻量,高效'
    })


if __name__ == '__main__':
    app.run()
