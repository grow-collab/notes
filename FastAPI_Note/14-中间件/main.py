import time

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import Response

app = FastAPI()


# 中间件(Middleware)：是处理请求和响应的钩子函数,位于客户端与视图函数之间
# 作用:可用于统一处理所有请求/响应（如认证、日志、添加公共响应头等）
# 执行流程:
# 客户端发来请求 -> 中间件(请求代码块) -> 路由系统 -> 数视图函 -> 中间件(响应代码块) -> 返回响应内容给客户端
# 假设有两个中间件m1和m2, 客户端请求 -> 'm1 request' -> 'm2 request' -> 'get_user函数执行' -> 'm2 response' -> 'm1 response' -> 返回响应内容给客户端
# 特点：请求阶段按中间件定义顺序执行，响应阶段按相反顺序执行（类似栈的先进后出）

# 定义HTTP中间件，通过@app.middleware('http')装饰器声明
# 参数说明：
#   - request: Request对象，包含客户端请求的所有信息（路径、参数、 headers等）
#   - call_next: 回调函数，用于调用下一个中间件或路由对应的视图函数
#                执行后返回视图函数的响应对象（Response）
@app.middleware('http')
async def m2(request: Request, call_next):
    # 请求代码块
    print('m2 request')

    response = await call_next(request)
    # 响应代码块
    response.headers['author'] = 'grow'
    print('m2 response')
    return response


@app.middleware('http')
async def m1(request: Request, call_next):
    # 请求代码块
    print('m1 request')
    # if request.client.host in ['127.0.0.1']:  # 黑名单
    #     return Response(content='visit forbidden')

    # if request.url.path in ['/user']:
    #     return Response(content='visit forbidden')

    start = time.time()
    response = await call_next(request)
    # 响应代码块
    print('m1 response')
    end = time.time()

    response.headers['ProcessTimer'] = str(end - start)
    return response


@app.get('/user')
async def get_user():
    time.sleep(3)
    print('get_user函数执行')
    return {'message': 'Hello World'}


@app.get('/items/{item_id}')
async def get_item(item_id: int):
    time.sleep(2)
    print('get_item函数执行')
    return {'item_id': item_id}


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, reload=True)
