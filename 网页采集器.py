import requests
if __name__ == '__main__':
    url = "https://www.baidu.com/s"
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    kw = input("enter a word:")
    parma = {
        "wd":kw
    }
    response = requests.get(url,params=parma,headers=headers)
    text = response.text

    filename = kw+".html"
    with open(filename,'w',encoding="utf-8") as f:
        f.write(text)
    print(filename,"保存成功")