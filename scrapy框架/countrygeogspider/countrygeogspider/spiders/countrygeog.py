import scrapy
from countrygeogspider.items import CountrygeogspiderItem
# 需求：爬取国家地理图片

class CountrygeogSpider(scrapy.Spider):
    name = 'countrygeog'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://m.dili360.com/Travel/sight/20201/1.htm']

    def parse_detial(self,response):
        img_final_src = response.xpath('//div[@class="img"]/img/@src | //div[@class="aImg"][1]/img[1]/@src').extract_first()
        print(img_final_src)
        item = response.meta['item']
        item['img_final_src']=img_final_src
        yield item
    def parse(self, response):
        baseurl = "http://m.dili360.com"
        item=CountrygeogspiderItem()
        li_list = response.xpath('//ul[@class="article-list"]/li')
        # print(li_list)
        for li in li_list:
            # print(li)
            img_src = baseurl+li.xpath('./div[1]/div[1]/a/@href').extract_first()
            # print(img_src)
            img_name = li.xpath('./div[2]/h3/a/text()')[0].extract()
            print(img_name)
            item['img_name']=img_name
            yield scrapy.Request(url=img_src,callback=self.parse_detial,meta={'item':item})
