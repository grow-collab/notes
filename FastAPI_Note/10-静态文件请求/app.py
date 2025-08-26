import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# 静态文件请求,将一个文件夹作为窗口开放,可以被外界访问的
# path:路由路径('/xxx',自定义)
# directory对应的参数,需要跟我们项目目录下的存放静态文件的文件夹的名字保持一致
app.mount('/static', StaticFiles(directory='static'))

if __name__ == '__main__':
    uvicorn.run('app:app', port=8000, reload=True)
