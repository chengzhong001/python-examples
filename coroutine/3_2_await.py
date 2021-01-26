'''
Description: 
Author: zhengchengzhong
Date: 2021-01-25 20:01:47
'''
import asyncio


async def other() -> str:
    print("start")
    await asyncio.sleep(2)
    print("end")
    return other.__name__

# await + 可等待对象（协程对象、Futrue、Task对象 -> IO等待）


async def func():
    print("hello world")
    response1 = await other()
    print("finish", response1)

    response2 = await other()
    print("finish", response2)

asyncio.run(func())
