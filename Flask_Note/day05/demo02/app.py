from flask import Flask, render_template, request, jsonify
from flask_migrate import Migrate
import config
from ext import db
import urls

# 项目重构
# 思路
#  1. 配置选项
#  2. 重构db ==> 模型
#  3. 路由与视图 ==> 蓝图文件
#  4. 迁移文件


app = Flask(__name__)  # 初始化的一个web服务
app.config.from_object(config)
app.register_blueprint(urls.bp)  # 注册蓝图
db.init_app(app)
migrate = Migrate(app, db)  # 数据迁移

if __name__ == '__main__':
    app.run()

# 表单验证
# 1.前端校验
# 2.后端校验
