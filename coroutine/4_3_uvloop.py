'''
Description: asyncio的替代方案 uvloop事件性能 > asyncio的事件循环
Author: zhengchengzhong
Date: 2021-01-25 23:36:24
'''
import asyncio
import uvloop

async def func():
    loop = asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    await asyncio.sleep(2)
    print(2)
    return func.__name__


asyncio.run(func())