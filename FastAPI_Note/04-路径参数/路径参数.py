from fastapi import FastAPI

app = FastAPI()

# 需要注意路由的顺序
@app.get('/user/1')
async def get_user():
    return {'user_id': 'root'}


# 04-路径参数 user_id 的值将作为参数传递给你的函数,用花括号 {}
@app.get('/user/{user_id}')
async def get_user(user_id: int): # user_id 被声明为 int 类型
    print(user_id)
    return {'user_id': user_id}


@app.get('/article/{article_id}')
async def get_article(article_id: int):
    print(article_id)
    return {'article_id': article_id}
