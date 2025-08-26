from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


# 宏
@app.route('/home/')
def home():
    return render_template('home.html')


# include语句与set语句
@app.route('/include/')
def include():
    return render_template('include.html')


# 模板继承 extends 页面复用
@app.route('/extends/')
def extends():
    return render_template('extends.html')



if __name__ == '__main__':
    app.run()
