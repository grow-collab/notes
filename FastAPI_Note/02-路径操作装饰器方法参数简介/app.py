import uvicorn
from fastapi import FastAPI

app = FastAPI()

# tags,标签
# deprecated,当接口不用时设置为True
@app.get('/get',tags=['get测试'],deprecated=True)
async def get_test():
    return {"method": "get方法"}


@app.get('/post')
async def post_test():
    return {"method": "post方法"}


@app.get('/put')
async def put_test():
    return {"method": "put方法"}


@app.get('/delete')
async def delete_test():
    return {"method": "delete方法"}


if __name__ == '__main__':
    uvicorn.run('app:app', port=8000, reload=True)
