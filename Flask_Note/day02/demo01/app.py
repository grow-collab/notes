from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


# 首页的路由与视图函数
@app.route('/index/')
def index():
    # 查询数据库中的数据(mysql sqlalchemy)==> 渲染到模板中
    context = {
        'name': '张三',
        'hobby': ['抽烟', '喝酒', '烫头']
    }
    # **context 解包==> name='张三'
    return render_template('index.html', **context)


# 过滤器: 对原有的值做一些处理,返回一些新的值 价格 99(int) ==> ¥99(字符串)


@app.route('/filter/')
def filter():
    context = {
        'position': -99,
        'signature': '哈哈哈',
        'html': '<h3>我是h3标签</h3>',
        'fruits': ['香蕉', '苹果', '火龙果', '西瓜', '南瓜'],
        'number': 66,
        'word': "Hello World",
        'case': '  happy new year  ',
        'price': 999,  # ¥999
        'create_time': datetime(2022, 8, 30, 21, 27, 30)
    }
    return render_template('filter.html', **context)


# 自定义过滤器
@app.template_filter('priceformat')
def price(value):
    price = '¥' + str(value)
    return price


# 时间过滤器
@app.template_filter('handle_time')
def handle_time(time):
    if isinstance(time, datetime):
        # <1分钟 ==> 刚刚
        # <1小时 ==> xx分钟前
        # <24小时 ==> xx小时前
        # <30天  ==> xx天前
        # 显示具体的时间 2022/07/19 20:30
        now = datetime.now()
        timestamp = (now - time).total_seconds()  # 拿到两个时间差的秒数
        if timestamp < 60:
            return '刚刚'
        elif timestamp >= 60 and timestamp < 60 * 60:
            minutes = int(timestamp / 60)
            return '%s 分钟前' % minutes
        elif timestamp >= 60 * 60 and timestamp < 60 * 60 * 24:
            hours = int(timestamp / (60 * 60))
            return '%s 小时前' % hours
        elif timestamp >= 60 * 60 * 24 and timestamp < 60 * 60 * 24 * 30:
            days = int(timestamp / (60 * 60 * 24))
            return '%s 天前' % days
        else:
            return time.strftime('%Y/%m/%d %H:%M')
    else:
        return time


if __name__ == '__main__':
    app.run()
