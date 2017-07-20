import asyncio
import time
import threading


async def async_foo():
    while True:
        print("async_foo started")
        await asyncio.sleep(1)
        print("async_foo done")

async def main():
    asyncio.ensure_future(async_foo())  # fire and forget async_foo()
    while True:
        asyncio.ensure_future(async_foo())  # fire and forget async_foo()
        print('Do some actions 1')
        await asyncio.sleep(1)
        print('Do some actions 2')
        await asyncio.sleep(1)
        print('Do some actions 3')
        await asyncio.sleep(1)

def job():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

def start():
    t = threading.Thread(target=job) 
    t.start()
    while True:
        print('main thread')
        time.sleep(1)



if __name__ == '__main__':
    start()
