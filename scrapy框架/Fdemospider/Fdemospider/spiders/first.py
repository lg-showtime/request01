import scrapy

class FirstSpider(scrapy.Spider):
    # 爬虫文件的名称：爬虫源文件的唯一标识
    name = 'first'
    # 允许的域名 用来限制start_url 列表中那些url可以进行请求发送
    # allowed_domains = ['www.xxx.com']
    # 起始的url列表；该列表存放的url会被scrapy 自动进行请求的发送
    start_urls = ['http://www.baidu.com/']
    # 用作与数据解析 response 参数表示就是请求成功后对应的响应对象
    def parse(self, response):
        print(response)