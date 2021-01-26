'''
Description: 
Author: zhengchengzhong
Date: 2021-01-25 22:48:11
'''
# 什么是异步迭代器
# 实现了 __aiter__() 和 __anext__() 方法的对象。__anext__必须返回一个awaitable对象，async for会处理异步迭代器的__anext__()方法所返回的可等待对象，直到其引发一个StopAsyncIteration异常。由 PEP 492 引入

# 什么是异步可迭代对象？
# 可在async for 语句中被使用的对象，必须通过他的 __aiter__() 方法返回 asynchronous iterator 由 PEP 492 引入


import asyncio


class Reader:
    def __init__(self) -> None:
        self.count = 0

    async def readline(self):
        self.count += 1
        if self.count == 100:
            return None
        return self.count

    def __aiter__(self):
        return self

    async def __anext__(self):
        val = await self.readline()
        if val == None:
            raise StopAsyncIteration
        return val
        

async def func():
    obj = Reader()
    async for item in obj:
        print(item)

asyncio.run(func())