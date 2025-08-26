from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr, validator
from typing import Optional, List
from datetime import date
import uvicorn


# 地址信息模型，用于存储省、市信息
class Addr(BaseModel):
    province: str
    city: str


# 数据校验(请求体)
# 模型之间可以嵌套（User模型中嵌套了Addr模型）
# 1. 创建一个类并继承BaseModel基类,将其作为视图函数的形参类型注解,FastAPI会自动基于该模型进行请求体数据校验和解析
# 2. 字段定义格式：字段名: 类型 = 要求(可设置默认值、校验规则等)
class User(BaseModel):
    name: str
    age: int = Field(default=18, gt=0, lt=120)
    email: EmailStr
    friends: List[int] = []
    birth: Optional[date] = None  # 等同于Union[date,None] = None
    address: Addr

    # 自定义验证逻辑
    @validator('name')
    def name_must_alpha(cls, value):
        assert value.isalpha()
        return value


class Data(BaseModel):
    data: List[User]


app = FastAPI()


@app.post('/user')
async def create_user(user: User):
    """
        创建用户接口
        接收符合User模型校验的请求体数据，返回接收到的用户信息
    """
    print(user, type(user))
    print(user.name, user.age, user.email, user.friends, user.birth, user.address)
    return user


@app.get('/data')
async def get_data(data: Data):
    return data


if __name__ == '__main__':
    uvicorn.run('数据校验:app', host='0.0.0.0', port=8000, reload=True)
