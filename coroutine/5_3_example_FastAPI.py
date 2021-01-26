'''
Description: 
Author: zhengchengzhong
Date: 2021-01-26 20:32:43
'''

import uvicorn
import asyncio
import aioredis

from pathlib import Path
from fastapi import FastAPI
from aioredis import Redis

# 创建一个redis连接池
redis_pool = aioredis.ConnectionsPool(
    "redis://localhost", password=None, minsize=1, maxsize=10)


app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello world"}


@app.get("/red")
async def red():
    print("request comming")
    await asyncio.sleep(3)
    # 连接池获取一个连接
    conn = await redis_pool.acquire()
    redis = Redis(conn)
    # 设置值
    await redis.hmset_dict("cat", key1=1, key2=2, key3=3)
    # 读取值
    result = await redis.hgetall("car", encoding="utf-8")
    print(result)
    # 连接池归还连接
    redis_pool.release(conn)
    return result


if __name__ == '__main__':
    # 脚本名称(5_3_example_FastAPI)：Path(__file__).stem
    uvicorn.run(Path(__file__).stem+":app", host="localhost",
                port=5000, log_level="info")
