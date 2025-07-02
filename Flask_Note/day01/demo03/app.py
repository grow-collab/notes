from flask import Flask, request
import uuid

print(uuid.uuid4())
app = Flask(__name__)


# url与视图
# http://flask.xxoutman.cn /question /19
# http://flask.xxoutman.cn /question /18
# http://flask.xxoutman.cn /question /17

# <id> ==> <converter:variable> ==> 类型别名(string):变量名称

# string类型
@app.route('/article/<id>')
def hello_world(id):
    # 查询数据库 id=77 文章内容
    return '当前,该篇文章的id是: ' + id


# int类型
@app.route('/number/<int:num>')
def number(num):
    print(type(num))
    return 'ok'


# float类型 ==> c c++ java 单精度浮点型(支持写小数点)
@app.route('/float/<float:dotnum>')
def dot(dotnum):
    return f'{dotnum}'


# uuid 类型 ==> 生成一个唯一的身份标识==> 淘宝==> 订单号==>重复??
@app.route('/uuid/<uuid:goods_id>')
def goods_id(goods_id):
    return f'唯一的身份标识: {goods_id}'


# path 类型 与string类型非常相似, 接受的参数可以传递/
@app.route('/path/<path:test>')
def path(test):
    return f'测试path: {test}'


# any类型 传入多种路径 /any/blog  /any/article
@app.route('/any/<any(blog,article,a,b,c):url_path>')
def test(url_path):
    return f'测试any: {url_path}'


# http://150.158.21.251:3300/search?key=许嵩
# 查询字符串
@app.route('/search/')
def search():
    result = request.args.get('key')
    print(result)
    return f'查询字符串的值是: {result}'


if __name__ == '__main__':
    app.run()
