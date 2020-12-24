import scrapy
from selenium import webdriver
from bilibiliPro.items import BilibiliproItem
# 需求爬取bilibili最热视频名称以及播放量
class BilibilihotSpider(scrapy.Spider):
    name = 'bilibilihot'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.bilibili.com/v/popular/all']

    def __init__(self):
        self.bro = webdriver.Chrome(executable_path="D:/Scrapy/request01/chromedriver")
    def parse(self, response):
        div_list = response.xpath('//*[@id="app"]/div[2]/div/ul/div')
        for div in div_list:
            video_url = "http:"+div.xpath('./div[1]/a/@href').extract_first()
            video_name = div.xpath('./div[2]/p/text()').extract_first()
            up_name = div.xpath('./div[2]/div/span[2]/span/text()').extract_first()
            video_playnum = div.xpath('./div[2]/div/p[1]/span[1]/text()').extract_first()
            video_playnum = video_playnum.split('\n')[1].strip()
            item = BilibiliproItem()
            item['video_url'] = video_url
            item['video_name'] = video_name
            item['up_name'] = up_name
            item['video_playnum'] = video_playnum

            yield item

    def closed(self,spider):
        self.bro.quit()