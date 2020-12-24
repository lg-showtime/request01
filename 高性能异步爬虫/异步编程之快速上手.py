import asyncio
async def func():
    print("let me see ")

result = func()
# 生成一个事件循环对象
loop = asyncio.get_event_loop()
# 将任务放置到这个任务列表中，然后就会自动执行
loop.run_until_complete(result)