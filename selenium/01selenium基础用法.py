from selenium import webdriver
from lxml import etree
import time
# 实例化一个浏览器对象
bor = webdriver.Chrome(executable_path="./chromedriver")

# 让浏览器发起一个指定url请求

bor.get('http://scxk.nmpa.gov.cn:81/xk/')
# 获取浏览器当前页码源码数据
page_text= bor.page_source

# 解析企业名称
tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@id="gzlist"]/li')
for li in li_list:
    name = li.xpath('./dl/@title')[0]
    print(name)

time.sleep(5)
bor.quit()