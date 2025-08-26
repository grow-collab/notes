import asyncio


async def download(name, sec):
    print(f'{name}开始下载')
    await asyncio.sleep(sec)  # 模拟异步等待(I/O)
    print(f'{name}下载完成')


# 第一种方法
# async def main():
#     # 创建三个任务,显示创建协程任务(类似调度)
#     task1 = asyncio.create_task(download('任务一', 2))
#     task2 = asyncio.create_task(download('任务二', 1))
#     task3 = asyncio.create_task(download('任务三', 3))
#
#     await task1
#     await task2
#     await task3

# 第二种方法
async def main():
    # 并发执行多个任务,收集返回值
    await asyncio.gather(
        download('任务1', 1),
        download('任务2', 1),
        download('任务3', 1),
    )


# 启动协程程序的主入口
asyncio.run(main())
