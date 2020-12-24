import requests
import re
import os
# 爬取图片
if __name__ == '__main__':
    if not os.path.exists("./tupian"):
        os.mkdir("./tupian")
    first_base_url = "https://www.qiushibaike.com/imgrank/page/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    for i in range(1,13):
        base_url = first_base_url+str(i)
        page_data = requests.get(base_url,headers = headers).text
        # print(page_data)
        ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
        # ex = re.compile(r'<div class="thumb">.*?<img src="(.*?)" alt.*?</div>')
        # image_list_src=re.findall(ex,page_data,re.S)
        image_list_src = re.findall(ex,page_data,re.S)
        # print(type(image_list_src))
        print("正在爬取第{}页".format(i))
        # for i in image_list_src:
            # print(i)
        # 遍历图片并且保存
        for src in image_list_src:
            url = "https:"+src
            image_data = requests.get(url,headers=headers).content
            # 保存图片
            image_name = src.split('/')[-1]
            image_path = "./tupian/"+image_name
            with open(image_path,'wb') as f:
                f.write(image_data)
                print(image_name,"保存成功")
    print("爬取完毕")