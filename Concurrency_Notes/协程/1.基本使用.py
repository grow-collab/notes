import asyncio


# async def 定义一个协程函数
# await 用于挂起协程(遇到I/O时让出控制权)
# asyncio.run()启动事件循环并运行主协程

async def spider():
    print('hello,world!')
    await asyncio.sleep(1)  # 模拟I/O操作
    print(1111)


asyncio.run(spider())
