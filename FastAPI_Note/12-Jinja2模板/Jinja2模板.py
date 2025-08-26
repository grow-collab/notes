import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

# 它的变量渲染,过滤器,控制结构与flask的模板语法基本一致

app = FastAPI()  # 实例化fastapi对象
templates = Jinja2Templates(directory='templates')  # 实例化Jinja2对象,并将文件夹路径设置为以templates命名的文件夹


@app.get('/index')
async def get_index(request: Request):
    name = '张三'
    age = 26

    context = {
        'request': request,  # 注意,返回模板响应时,必须有request键值对,且值为Request请求对象
        'name': name,
        'age': age,
        'books': ['西游记', '红楼梦', '三国演义', '水浒传'],
        'info': {
            '西游记': {'price': 39.9, 'publish': '苹果出版社'},
            '水浒传': {'price': 36.8, 'publish': '橘子出版社'}
        },
        'test': [1, 2, 3, 4, 5, 6]
    }  # context上下文对象,一个字典
    return templates.TemplateResponse('index.html', context)


if __name__ == '__main__':
    uvicorn.run('Jinja2模板:app', port=8000, reload=True)
