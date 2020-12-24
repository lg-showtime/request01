import requests
import json
# 存储数据
def savedata(data_json):
    fp = open("./douban.json", 'a', encoding='utf-8')
    fp.write(",")
    json.dump(data_json, fp=fp, ensure_ascii=False)

# 单次请求解析
def request_get(headers,base_url,start_num):
    parma = {
        'type': '24',
        'interval_id': '100:90',
        'action': '',
        'start': str(start_num),
        'limit': '100'
    }
    response = requests.get(base_url, params=parma, headers=headers)
    data_json = response.json()
    return data_json
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    base_url = "https://movie.douban.com/j/chart/top_list?"
    start_num = 0
    data_json = request_get(headers, base_url, start_num)
    while data_json !=[]:
        print(data_json)
        # 持久化存储
        savedata(data_json)
        start_num = start_num + 100
        data_json = request_get(headers, base_url, start_num)
    print("over")