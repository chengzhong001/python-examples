'''
Description: 
Author: zhengchengzhong
Date: 2021-01-25 22:16:54
'''
import time
import asyncio
import concurrent.futures



def func():
    time.sleep(2)
    return "hello world"

async def main():
    loop = asyncio.get_event_loop()

    # 1.run in the default loop's executor(默认ThreadPoolExecutor)
    # 第一步：内部会先调用ThreadPoolExecutor 的submit方法取线程池中申请一个线程执行func函数，并返回一个concurrent.futures.Future 对象
    # 第二步：调用 asyncio.wrap_future 将 concurrent.futures.Future 包装为 asyncio.Future
    # 注解：因为 concurrent.futures.Future 对象不支持 await 语法，所以需要包装 asyncio.Future 对象才能使用
    future = loop.run_in_executor(None, func)
    result = await future
    print("default thread pool:", result)

    # 2.Run in a customer thread pool
    pool = concurrent.futures.ThreadPoolExecutor()
    result = await loop.run_in_executor(pool, func)
    print("custom thread pool:", result)

    # 3.Run in a customer process pool
    # pool = concurrent.futures.ProcessPoolExecutor()
    # result = await loop.run_in_executor(pool, func)
    # print("custom process pool:", result)


asyncio.run(main())