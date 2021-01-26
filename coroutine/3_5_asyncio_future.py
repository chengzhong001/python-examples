'''
Description: Task的集成Future，Task对象内部await的结果的处理基于Future
Author: zhengchengzhong
Date: 2021-01-25 21:41:05
'''

import asyncio
from asyncio import Future


async def set_after(future: Future):
    await asyncio.sleep(2)
    future.set_result("6666")
    print("finish")


async def main():
    # 获取当前事件循环
    loop = asyncio.get_running_loop()
    
    # 创建一个任务（Future），没设定任何行为，则这个任务永远不知道什么时候结束
    future = loop.create_future()

    # 手动创建一个任务，绑定set_after函数,函数内部2s之后会给future赋值
    # 手动设置future最终结果，那么future就可以结束了
    await loop.create_task(set_after(future))

    await future

asyncio.run(main())
