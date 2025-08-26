# 一对一  name= db.relationship('User',backref=db.backref('xx',uselist=False))

# 一对多  name= db.relationship('User',backref="xx")

# 多对多  学生与选课 中间关联表
