import asyncio


async def get_result():
    await asyncio.sleep(1)
    return '结果123'


async def main():
    result = await get_result()
    print(result)


asyncio.run(main())
