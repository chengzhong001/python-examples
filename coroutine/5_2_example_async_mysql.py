'''
Description: 
Author: zhengchengzhong
Date: 2021-01-26 20:14:14
'''
import asyncio
import aiomysql
from aiomysql import cursors


async def execute():
    # 网络IO操作，连接mysql
    conn = await aiomysql.connect(host="localhost",
                                  port=3306,
                                  user="root",
                                  password="0501Zhong,.")
    # 网络IO操作，创建cursor
    cursor = await conn.cursor()
    # 网络IO操作,执行SQL
    await cursor.execute("select host, user, select_priv from mysql.user")
    # 网络IO操作，获取结果
    result = await cursor.fetchall()
    print(result)
    # 网络IO操作，关闭连接
    await cursor.close()
    conn.close()

task_list = [execute(), execute(), execute()]
asyncio.run(asyncio.wait(task_list))

# asyncio.run(execute())
