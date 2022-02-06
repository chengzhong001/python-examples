'''
Description: 
Author: zhengchengzhong
Date: 2021-02-27 10:12:37
Reference: https://mp.weixin.qq.com/s?__biz=MzIxMjY5NTE0MA==&mid=2247483720&idx=1&sn=f016c06ddd17765fd50b705fed64429c
'''
import socket
import time
import ssl


def blocking_way():
    sock = ssl.wrap_socket(socket.socket())
    sock.connect(('www.example.org', 443))  # host.com
    request = "GET / HTTP/1.1\r\nHOST: www.example.org\r\nConnection: close\r\n\r\n"
    sock.send(request.encode())
    response = bytes()
    chunk = sock.recv(1024)
    while chunk:
        response += chunk
        chunk = sock.recv(1024)
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
