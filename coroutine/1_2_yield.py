'''
Description: 
Author: zhengchengzhong
Date: 2021-01-24 14:31:59
'''


def func1():
    yield 1
    yield from func2()
    yield 2

def func2():
    yield 3
    yield 4

f1 = func1()
for item in f1:
    print(item)