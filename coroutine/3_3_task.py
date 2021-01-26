'''
Description: 在事件循环中添加多个任务
Author: zhengchengzhong
Date: 2021-01-25 20:18:33
'''
import asyncio


async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return func.__name__


async def main():
    print("main start")
    # 创建task对象，将当前执行func函数任务添加到事件讯息
    task1 = asyncio.create_task(func())
    task2 = asyncio.create_task(func())

    print("main end")

    # 当执行某协程遇到io操作时，会自动化切换执行其他任务
    # 此处的await是等待相对应的协程全部执行完毕并获取结束
    ret1 = await task1
    ret2 = await task2
    print(ret1, ret2)

# 第一种写法
async def main():
    print("main start")
    # 创建task对象，将当前执行func函数任务添加到事件讯息
    task_list = [asyncio.create_task(func(), name="func1"),
                 asyncio.create_task(func(), name="func2")]
    print("main end")

    # 当执行某协程遇到io操作时，会自动化切换执行其他任务
    # 此处的await是等待相对应的协程全部执行完毕并获取结束
    done, pending = await asyncio.wait(task_list)
    result = [{i.get_name(), i.result()} for i in done]  #3.8版本之后获取get_name()
    print(result, pending)
asyncio.run(main())

# 第二种写法
task_list = [func(), func()]
done, pending = asyncio.run(asyncio.wait(task_list))