import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Union


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr


# 响应模型
class UserOut(BaseModel):
    username: str
    email: EmailStr


# 商品的响应模型
class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: float = 10.5
    tags: list[str] = []


app = FastAPI()


# 执行逻辑,正常生产过程是不需要返回密码的
# 1.首先接收到前端传来的数据,通过'UserIn'模型进行校验
# 2.如果校验通过,把数据给到 'user' 对象
# 3.正常我们是直接返回,但是路由路径'response_model'参数添加了一个响应模型'UserOut',所以需要通过'UserOut'模型过滤一下在返回
@app.post('/user', response_model=UserOut)
async def get_user(user: UserIn):
    # 数据库添加操作
    return user


items = {
    'foo': {'name': 'Foo', 'price': 10.9},
    'bar': {'name': 'Bar', 'description': 'baz', 'price': 20.5, 'tax': 20.2},
    'baz': {'name': 'Baz', 'description': None, 'price': 99.6, 'tax': 11.9, 'tags': []}
}


# 排除(exclude)和包括(include)
# response_model_exclude_unset,不返回是默认值的和None的字段
# response_model_exclude_defaults,不返回是默认值的字段
# response_model_exclude_none,不返回是None的字段
# response_model_include = {'name','price'},要求输出指定字段
# response_model_exclude = {'tags'},要求输出排除指定字段
@app.post('/item/{item_id}', response_model=Item, response_model_exclude_unset=True)
async def get_item(item_id: str):
    return items[item_id]


'''
item_id = foo
返回结果(response_model_exclude_unset=False),不添加此字段也是默认为False:
{
  "name": "Foo",
  "description": null,
  "price": 10.9,
  "tax": 10.5,
  "tags": []
}

返回结果(response_model_exclude_unset=True):
{
  "name": "Foo",
  "price": 10.9
}
'''

if __name__ == '__main__':
    uvicorn.run('app:app', port=8000, reload=True)
