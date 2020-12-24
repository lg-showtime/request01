#  协程是啥？
# 协程是在单线程中遇到io请求去切换代码块执行的一种技术

import asyncio

async def func1():
    print("事件1")
    await asyncio.sleep(2)

    print("事件1完成")

async def func2():
    print("事件2")
    await asyncio.sleep(2)
    print("事件2完成")

task = [
    asyncio.ensure_future(func1()),
    asyncio.ensure_future(func2())
    ]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(task))
# asyncio.run(asyncio.wait(task))

