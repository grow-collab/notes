from flask import Flask, render_template, redirect, url_for
from db import cursor

app = Flask(__name__)


@app.route('/')
def home():
    return redirect(url_for('index'))


@app.route('/index/')
def index():
    # 查询数据库 ( flask-sqlalchemy ==> (orm模型))
    # pymysql ==> sql
    sql = '''select count(cn_name) AS count,round(avg(grade),2) AS comments  from movices;'''
    cursor.execute(sql)
    datas = cursor.fetchall()
    # print(datas)
    return render_template('index.html', **datas[0])


# 评分页面
@app.route('/score/')
def score():
    # 查询数据库
    sql = '''select grade ,count(grade) AS total from movices group by grade;'''
    cursor.execute(sql)
    datas = cursor.fetchall()
    print(datas)
    scores = []  # 评分数据 # ['8.4','8.5','8.6']
    numbers = []  # 评分数量电影数据 # [1,11,22]
    for data in datas:
        scores.append(data['grade'])
        numbers.append(data['total'])

    return render_template('score.html', scores=scores, numbers=numbers)


if __name__ == '__main__':
    app.run()
