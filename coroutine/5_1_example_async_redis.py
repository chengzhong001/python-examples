'''
Description: python操作redis时，连接/操作/断开都是网络IO
Author: zhengchengzhong
Date: 2021-01-26 19:54:24
'''
import aioredis
import asyncio


async def execute(address, password):
    print("start executing", address)
    # 网络IO操作，创建redis连接
    redis = await aioredis.create_redis(address=address, password=password)
    # 网络IO操作：redis中设置hash值car，内部设置三个键值对
    await redis.hmset_dict("car", key1=1, key2=2, key3=3)
    # 网络IO操作，redis中获取值
    result = await redis.hgetall("car", encoding="utf-8")
    print(result)

    redis.close()
    # 网络IO操作，关闭redis连接
    await redis.wait_closed()
    print("finished", address)

task_list = [execute("redis://localhost", None),
             execute("redis://localhost", None)]

# asyncio.run(execute("redis://localhost", None))
asyncio.run(asyncio.wait(task_list))
