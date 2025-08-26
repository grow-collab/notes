import requests
import asyncio  # 用于调度协程,启动事件循环
import httpx  # 支持同步和异步两种模式
import time


# 一.同步请求
# def fetch(url):
#     response = requests.get(url)
#     print(f'{url}状态码:{response.status_code}')
#     return response.text
#
#
# def main():
#     urls = ['https://httpbin.org/delay/2', 'https://httpbin.org/delay/2', 'https://httpbin.org/delay/2']
#     start = time.time()
#     for url in urls:
#         fetch(url)
#     end = time.time()
#     print(f'同步耗时:{end - start:.2f}秒')
#
# main()


# 二.异步请求
async def fetch1(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        print(f'{url}状态码:{response.status_code}')
        return response.text


async def main1():
    urls = ['https://httpbin.org/delay/2', 'https://httpbin.org/delay/2', 'https://httpbin.org/delay/2']
    start = time.time()
    tasks = [fetch1(url) for url in urls]
    await asyncio.gather(*tasks)
    end = time.time()
    print(f'异步耗时:{end - start:.2f}秒')


asyncio.run(main1())
