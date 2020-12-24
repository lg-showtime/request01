import scrapy
from selenium import webdriver
from wangyiPro.items import WangyiproItem
class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://news.163.com/']
    model_urls =[] # 五个板块对应的详情页面得url

    # 实例化一个浏览器对象
    def __init__(self):
        self.bro = webdriver.Chrome(executable_path='D:/Scrapy/request01/chromedriver')
    def parse(self, response):
        li_list = response.xpath('//*[@id="index2016_wrap"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/ul/li')
        alist = [3,4,6,7,8]
        for index in alist:
            model_url = li_list[index].xpath('./a/@href').extract_first()
            self.model_urls.append(model_url)

        # 依次对每一个板块对应的页面进行请求
        for url in self.model_urls:
            yield scrapy.Request(url=url,callback=self.parse_model)

    # 每一个板块对应的新闻标题的内容都是动态加载的
    def parse_model(self,response):
        div_list= response.xpath('/html/body/div/div[3]/div[4]/div[1]/div/div/ul/li/div/div')
        for div in div_list:
            title = div.xpath('./div/div[1]/h3/a/text()').extract_first()
            new_detail_url = div.xpath('./div/div[1]/h3/a/@href').extract_first()

            item = WangyiproItem()
            item['title'] = title
            # 对新闻得url 发起请求
            yield scrapy.Request(url=new_detail_url,callback=self.parse_detail,meta={'item':item})
    def parse_detail(self,response):
        content = response.xpath('//*[@id="endText"]//text()').extract()
        content = ''.join(content)
        item = response.meta['item']
        item['content'] = content

        yield item

    def closed(self, spider):
        self.bro.quit()