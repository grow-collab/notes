import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS组件实现跨域请求
origins = ['http://localhost:63342']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # *代表所有客户端
    allow_credentials=True,
    allow_methods=['GET', 'POST'],
    allow_headers=['*']
)


# @app.middleware('http')
# async def CORSMiddleware(request: Request, call_next):
#     response = await call_next(request)
#     # 响应代码块
#     response.headers['Access-Control-Allow-Origin'] = '*'  # *代表允许所有的客户端访问
#     return response


@app.get('/user')
async def get_user():
    return {'message': 'grow'}


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, reload=True)
