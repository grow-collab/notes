from fastapi import APIRouter

user = APIRouter() # 子路由对象


@user.get('/login')
async def user_login():
    return {'user': 'login'}


@user.get('/register')
async def user_register():
    return {'user': 'register'}
