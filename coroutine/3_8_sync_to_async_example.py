'''
Description: 
Author: zhengchengzhong
Date: 2021-01-25 22:37:08
'''

import asyncio
import requests
from requests.models import Response
import time

async def download_image(url: str):
    print("start download", url)
    loop = asyncio.get_event_loop()

    future = loop.run_in_executor(None, requests.get, url)

    response = await future
    print("finish download")
    file_name = url.split('/')[-1]
    with open(file_name, "wb") as file:
        file.write(response.content)


if __name__ == '__main__':
    urls = [
        "https://p1.meituan.net/travelcube/bc37e161d36e270a57e317c74e4a03dd928392.png",
        "https://p0.meituan.net/travelcube/71675acb360c5674dadd44e67170bfd5222012.png",
        "https://p0.meituan.net/travelcube/3a47eb75bb2105f235d9fd2423976026754002.png",
        "https://p1.meituan.net/travelcube/0100d4044ad084afbf6b395a6bc3053e687520.png",
        "https://p0.meituan.net/travelcube/77f9db3619dc7ff5514309a98ab475e937708.png",
        "https://p0.meituan.net/travelcube/212ceb5cd1106885a450c30afc8fc01062120.webp"
    ]
    start_time = time.time()
    tasks = [download_image(url) for url in urls]
    loop = asyncio.run(asyncio.wait(tasks))
    end_time = time.time()
    print(end_time-start_time)
