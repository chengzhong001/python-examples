'''
Description: 
Author: zhengchengzhong
Date: 2021-02-27 12:05:05
Reference: https://mp.weixin.qq.com/s?__biz=MzIxMjY5NTE0MA==&mid=2247483720&idx=1&sn=f016c06ddd17765fd50b705fed64429c
'''
import socket
import ssl
import time
from typing import Tuple


def blocking_way():
    sock = ssl.wrap_socket(socket.socket())
    sock.setblocking(False)
    try:
        sock.connect(('www.example.org', 443))  # host.com
    except Exception as error:
        pass
    request = "GET / HTTP/1.1\r\nHOST: www.example.org\r\nConnection: close\r\n\r\n"
   
    data = request.encode()

    while True:
        try:
            sock.send(data)
            break
        except Exception as error:
            pass

    response = bytes()
    while True:
        try:
            chunk = sock.recv(1024)
            while chunk:
                response += chunk
                # print(response)
                chunk = sock.recv(1024)
            break
        except Exception as error:
            pass
        
    print(response.decode())
    return response


def sync_way():
    res = []
    for i in range(10):
        res.append(blocking_way())
    return len(res)


if __name__ == '__main__':
    start_time = time.time()
    sync_way()
    end_time = time.time()
    print("time-consuming: ", end_time-start_time)
