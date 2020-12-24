import asyncio

async def request(url):
    print("正在请求的url是",url)
    print("请求成功",url)
    return url
c = request("www.baidu.com")
# # async 修饰的函数为协程函数，调用后返回协程对象
# c = request("www.baidu.com")
# # 创建一个事件循环对象
# loop = asyncio.get_event_loop()
# # 将携程对象注册到loop，然后启动事件循环
# loop.run_until_complete(c)

# task使用
# loop = asyncio.get_event_loop()
# # 基于loop创建一个task对象
# task = loop.create_task(c)
# print(task)
# loop.run_until_complete(task)
# print(task)


# future对象使用,future对象和task 本质上差不多
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(c)
# loop.run_until_complete(task)


def callback_func(task):
    # result返回的就是任务对象中封装的协程对象对应函数的返回值
    print(task.result())
# 绑定回调
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(c)
# 将回调函数绑定到任务对象中
task.add_done_callback(callback_func)
loop.run_until_complete(task)