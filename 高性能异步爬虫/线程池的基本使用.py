import requests
import time
# 导入线程池模块对应的类
from multiprocessing.dummy import Pool
# 使用线程池方式执行
start_time = time.time()
def get_page(str):
    print("正在下载：",str)
    time.sleep(2)
    print("下载成功：",str)

name_list = ['xiaomin','dfs','sfds','ss']

# 实例化一个线程池对象
pool = Pool(4)
# 将列表中的每一个元素传递到get_page进行处理
pool.map(get_page,name_list)

end_time = time.time()

print(end_time - start_time)