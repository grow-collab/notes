import asyncio
import httpx


async def fetch(url):
    # 连接池复用,tcp连接,提高效率
    async with httpx.AsyncClient() as client:
        response = await client.get(url)  # await的作用:挂起当前协程的执行,等待某个'异步任务'完成,然后恢复继续执行
        # 解析数据
        json_data = response.json()
        origin = json_data['origin']  # ip地址
        url = json_data['url']
        print(f'{url}状态码:{response.status_code},IP地址:{origin}')


async def main():
    urls = ['https://httpbin.org/delay/2', 'https://httpbin.org/get']
    # 创建任务队列
    tasks = [fetch(url) for url in urls]
    # 并发执行多个任务,收集返回值
    await asyncio.gather(*tasks)


asyncio.run(main())
