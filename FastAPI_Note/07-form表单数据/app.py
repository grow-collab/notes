import uvicorn
from fastapi import FastAPI, Form

app = FastAPI()


# fastapi使用Form组件来接收数据,需要先使用 'pip install python-multipart' 命令进行安装
@app.post('/regin')
async def regin(email: str = Form(), password: str = Form()):
    print(f'邮箱: {email},密码: {password}')
    # 注册实现数据库的添加操作
    return {'邮箱': email}

if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0', port=8000, reload=True)
