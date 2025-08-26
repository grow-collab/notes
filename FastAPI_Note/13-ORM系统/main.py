from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from settings import TORTOISE_ORM
from api.student import student_router
import uvicorn

app = FastAPI()
app.include_router(student_router, prefix='/student', tags=['选课系统的学生接口'])

# 该方法会在fastapi启动时触发,内部通过传递进去的app对象,监听服务启动和终止事件
# 当检测到启动事件时,会初始化Tortoise对象,如果generate_schemas为True则还会进行数据迁移
# 当检测到终止事件时,会关闭连接
register_tortoise(app=app, config=TORTOISE_ORM)


@app.get('/')
async def root():
    return {'message': 'Hello, World!'}


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, reload=True)
