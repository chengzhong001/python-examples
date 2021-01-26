'''
Description: 
Author: zhengchengzhong
Date: 2021-01-24 14:11:35
'''
from greenlet import greenlet


def func1():
    print(1)
    #g2.switch()
    print(2)
    #g2.switch()

def func2():
    print(3)
    #g1.switch()
    print(4)



gr1 = greenlet(func1)
gr2 = greenlet(func2)

gr1.switch()
