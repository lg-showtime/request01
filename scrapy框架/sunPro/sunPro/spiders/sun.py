import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from time import sleep
from sunPro.items import SunproItem,DetailItem


class SunSpider(CrawlSpider):
    name = 'sun'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://wzzdg.sun0769.com/political/index/politicsNewest?id=1&page=0']

    # 链接提取器：根据指定规则（allow = "正则"）进行指定连接的提取
    link = LinkExtractor(allow=r'id=1&page=\d+')
    link_detail = LinkExtractor(allow=r'political/politics/index\?id=\d+')
    rules = (
        # 规则解析器:将链接提取器提取到的连接进行指定规则的解析操作
        Rule(link, callback='parse_item', follow=True),
        # follow=True 可以将链接提取器 继续作用到 连接提取器提取到的链接 所对应的的页面当中
        Rule(link_detail,callback='parse_detail')
    )
    # 以下两个解析方法中是不可以实现请求传参的
    # 无法将两个解析方法的数据存储到同一个item中，因此可以存储到两个item中
    def parse_item(self, response):
        sleep(1)
        # 注意;xpath 表达式中不剋出现tbody标签
        li_list= response.xpath('/html/body/div[2]/div[3]/ul[2]/li')

        for li in li_list:
            new_num = li.xpath('./span[1]/text()').extract_first()
            new_title = li.xpath('./span[3]/a/text()').extract_first()
            # print(new_num,new_title)
            item = SunproItem()
            item['title'] = new_title
            item['new_num'] =new_num

            yield item
    def parse_detail(self,response):
        sleep(1)
        print(response)
        new_id = response.xpath('/html/body/div[3]/div[2]/div[2]/div[1]/span[4]/text()').extract_first()
        new_content = response.xpath('/html/body/div[3]/div[2]/div[2]/div[2]//text()').extract()
        new_content = ''.join(new_content)
        # print(new_id,new_content)
        item = DetailItem()
        item['content']=new_content
        item['new_id']=new_id

        yield item
