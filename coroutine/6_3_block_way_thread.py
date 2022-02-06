'''
Description: 
Author: zhengchengzhong
Date: 2021-02-27 11:27:09
Reference: https://mp.weixin.qq.com/s?__biz=MzIxMjY5NTE0MA==&mid=2247483720&idx=1&sn=f016c06ddd17765fd50b705fed64429c
'''
import socket
import ssl
from concurrent import futures
import time


def blocking_way():
    sock = ssl.wrap_socket(socket.socket())
    sock.connect(('www.example.org', 443))  # host.com
    request = "GET / HTTP/1.1\r\nHOST: www.example.org\r\nConnection: close\r\n\r\n"
    sock.send(request.encode())
    response = bytes()
    chunk = sock.recv(4096)
    while chunk:
        response += chunk
        chunk = sock.recv(4096)
    print(response.decode())
    return response



def process_way():
    workers = 10
    with futures.ThreadPoolExecutor(workers) as executor:
        futs = {executor.submit(blocking_way) for i in range(10)}
    return len([fut.result() for fut in futs])


if __name__ == '__main__':
    start_time = time.time()
    process_way()
    end_time = time.time()
    print("time-consuming: ", end_time-start_time)
