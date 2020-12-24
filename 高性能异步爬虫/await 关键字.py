# await 关键字
import asyncio
async def others():
    print("start")
    await asyncio.sleep(2)
    print("end")
    return "返回值"

async def func():
    print("执行协程函数内部代码")
    response1 = await others()
    print("IO请求结束，结果为",response1)
    
    response2 = await  others()
    print("IO请求结束，结果为",response2)

asyncio.run(func())