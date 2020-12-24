# 需求 进行三国演义小说爬取并保存
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    base_url = "https://www.shicimingju.com/book/sanguoyanyi.html"

    page_text = requests.get(base_url,headers=headers).text
    # 实例化Beautifulsoup 对象
    soup = BeautifulSoup(page_text,'lxml')
    # 解析数据
    page_list = soup.select('.book-mulu > ul > li')
    fp = open('./sanguo.txt','w',encoding='utf-8')
    for list in page_list:
        # print(list.string)
        title = list.a.string
        datile_page_url = "https://www.shicimingju.com"+list.a['href']
        datile_page_text = requests.get(datile_page_url,headers=headers).text
        text_soup = BeautifulSoup(datile_page_text,'lxml')
        datile_tag= text_soup.find('div',class_='chapter_content')
        datile_text = datile_tag.text
        fp.write(title+':'+datile_text+'\n')
        print(title,"保存完毕")