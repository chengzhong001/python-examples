'''
Description: 
Author: zhengchengzhong
Date: 2021-01-24 21:05:30
'''
import httpx
import asyncio
import time


async def fetch(session: httpx.AsyncClient, url: str):
    print("发送请求:", url)
    start_time = time.time()
    response = await session.get(url)
    content = response.content
    file_name = url.split('/')[-1]
    with open(file_name, "wb") as file:
        file.write(content)
    end_time = time.time()
    print(end_time-start_time)


async def main():
    async with httpx.AsyncClient() as session:
        urls = [
            "https://p1.meituan.net/travelcube/bc37e161d36e270a57e317c74e4a03dd928392.png",
            "https://p0.meituan.net/travelcube/71675acb360c5674dadd44e67170bfd5222012.png",
            "https://p0.meituan.net/travelcube/3a47eb75bb2105f235d9fd2423976026754002.png",
            "https://p1.meituan.net/travelcube/0100d4044ad084afbf6b395a6bc3053e687520.png",
            "https://p0.meituan.net/travelcube/77f9db3619dc7ff5514309a98ab475e937708.png",
            "https://p0.meituan.net/travelcube/212ceb5cd1106885a450c30afc8fc01062120.webp"
        ]
        tasks = [asyncio.create_task(fetch(session, url)) for url in urls]
        await asyncio.wait(tasks)

if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())
    end_time = time.time()
    print("consuming time for downloading all images: ", end_time-start_time)

