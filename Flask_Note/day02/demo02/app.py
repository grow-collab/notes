from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/control/')
def control():
    context = {
        "obj": {"sick": False, "headache": True},
        "users": [{'username': '罗翔', 'age': 18}, {'username': '刑法', 'age': 68}, {'username': '法外狂徒', 'age': 12}],
        'dic': {'name': '疾风剑豪', 'age': 10},
        'books': [
            {
                'name': '三国演义',
                'author': '罗贯中',
                'price': 100
            },
            {
                'name': '西游记',
                'author': '吴承恩',
                'price': 99
            },
            {
                'name': '红楼梦',
                'author': '曹雪芹',
                'price': 199
            },
            {
                'name': '水浒传',
                'author': '施耐庵',
                'price': 169
            }
        ]
    }
    return render_template('control.html', **context)


if __name__ == '__main__':
    app.run()
