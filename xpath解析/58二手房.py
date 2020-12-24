import requests
from lxml import etree

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    url = "https://sanhe.58.com/ershoufang/"

    page_text = requests.get(url=url,headers=headers).text
    #数据解析
    tree = etree.HTML(page_text)
    list = tree.xpath('//ul[@class="house-list-wrap"]/li')
    fp =open('./58.txt','w',encoding='utf-8')
    for li in list:
        title = li.xpath('./div[@class="list-info"]/h2/a/text()')[0]
        print(title)
        fp.write(title+"\n")