'''
Description: 
Author: zhengchengzhong
Date: 2021-01-25 19:57:35
'''
import asyncio


async def func():
    print("hello world")

loop = asyncio.get_event_loop()
loop.run_until_complete(func())
