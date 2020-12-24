import requests
from lxml import etree
import os
if __name__ == '__main__':
    if not os.path.exists("./meimv"):
        os.mkdir("./meinv")
    url = "http://pic.netbian.com/4kmeinv/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    page_text = requests.get(url=url,headers=headers).text

    tree = etree.HTML(page_text)

    li_list = tree.xpath('//div[@class="slist"]//li')
    for li in li_list:
        img_src = "http://pic.netbian.com"+li.xpath('./a/img/@src')[0]
        img_title = li.xpath('./a/img/@alt')[0]+'.jpg'
        # 解决乱码的通用解决办法
        img_title = img_title.encode('iso-8859-1').decode('gbk')

        print(img_src,img_title)
        #请求图片进行持久化存储

        img_data = requests.get(url=img_src,headers=headers).content
        img_path = 'meinv/'+img_title
        with open(img_path,'wb')as fp:
            fp.write(img_data)
            print(img_title,"下载完毕")
