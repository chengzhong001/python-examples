'''
Description: 
Author: zhengchengzhong
Date: 2021-01-25 23:01:56
'''
# 此种对象通过定义 __aenter__() 和__aexit() 方法来对 async for 语句中的环境进行控制，由 PEP 492 引入

import asyncio


class AsyncContextManager:
    def __init__(self) -> None:
        self.conn = None

    async def do_something(self):
        return 666

    async def __aenter__(self):
        self.conn = await asyncio.sleep(1)
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await asyncio.sleep(1)


async def func():
    async with AsyncContextManager() as func:
        result = await func.do_something()
        print(result)


asyncio.run(func())
