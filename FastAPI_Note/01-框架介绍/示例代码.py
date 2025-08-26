from typing import Union

from fastapi import FastAPI

# 所有的路由、中间件、事件处理等都将基于该实例进行配置
app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
