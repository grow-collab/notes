from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

# Request对象
@app.post('/items')
async def get_items(request: Request):
    print('URL:', request.url)
    print('客户端IP地址:', request.client.host)
    print('客户端宿主:', request.headers.get('User-Agent'))
    print('Cookies:', request.cookies) # COOKIE:a=1

    return {
        'URL:': request.url,
        '客户端IP地址:': request.client.host,
        '客户端宿主:': request.headers.get('User-Agent'),
        'Cookies:': request.cookies
    }


if __name__ == '__main__':
    uvicorn.run('app:app', port=8000, reload=True)
