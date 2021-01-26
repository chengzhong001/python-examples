'''
Description: 使用线程池进程池操作对象
Author: zhengchengzhong
Date: 2021-01-25 22:03:00
'''

import time
from concurrent.futures import Future
from concurrent.futures.thread import ThreadPoolExecutor    
from concurrent.futures.process import ProcessPoolExecutor  

#创建线程池
thread_pool = ThreadPoolExecutor(max_workers=5)

# 创建进程
process_pool = ProcessPoolExecutor(max_workers=5)

def func(value):
    time.sleep(2)
    print(value)
    return 123

for i in range(10):
    future = thread_pool.submit(func, i)
    print(future)

