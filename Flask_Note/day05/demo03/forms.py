import wtforms
from wtforms.validators import length, email, EqualTo


# 登录校验器
class LoginForm(wtforms.Form):
    email = wtforms.StringField('用户名', validators=[length(min=4, max=20), email()])
    password = wtforms.StringField('密码', validators=[length(min=6, max=12)])


# 注册校验器
class RegisterForm(wtforms.Form):
    name = wtforms.StringField('用户名', validators=[length(min=4, max=25)])
    email = wtforms.StringField('邮箱', validators=[email()])
    password = wtforms.StringField('密码', validators=[length(min=6, max=20)])
    password_confirm = wtforms.StringField('确认密码', validators=[EqualTo('password')])
