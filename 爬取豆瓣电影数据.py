import requests
import json
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    base_url = "https://movie.douban.com/j/chart/top_list?"
    parma = {
        'type': '24',
        'interval_id': '100:90',
        'action':'',
        'start': '0',
        'limit': '20'
    }
    response = requests.get(base_url,params=parma,headers=headers)
    data_json= response.json()
    # 持久化存储
    fp = open("./douban.json",'w',encoding='utf-8')
    json.dump(data_json,fp=fp,ensure_ascii=False)

    print("over")