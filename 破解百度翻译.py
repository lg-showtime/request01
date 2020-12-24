import requests
import json
if __name__ == '__main__':
    post_url = "https://fanyi.baidu.com/sug"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    kw = input("enter a words:")
    data = {
        'kw':kw
    }
    response = requests.post(url=post_url,data=data,headers=headers)
    #json 返回的是一个对象
    dict_obj = response.json()
    # print(dict_obj)
    # print(type(dict_obj)) 字典类型
    # 持久化存储
    filename = kw+'.json'
    fp = open(filename,'w',encoding='utf-8')
    json.dump(dict_obj,fp=fp,ensure_ascii=False)

    print("保存成功")

