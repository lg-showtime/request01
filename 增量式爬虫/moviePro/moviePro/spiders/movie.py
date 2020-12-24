import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from redis import Redis
from moviePro.items import MovieproItem
from time import sleep
class MovieSpider(CrawlSpider):
    name = 'movie'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.4567kan.com/frim/index1.html']

    rules = (
        Rule(LinkExtractor(allow=r'/frim/index1-\d+\.html'), callback='parse_item', follow=True),
    )
    # 创建redis连接对象
    conn = Redis(host='127.0.0.1',port=6379)
    def parse_item(self, response):
        li_list = response.xpath('/html/body/div[1]/div/div/div/div[2]/ul/li')
        for li in li_list:
            # 获取详情页的url
            # sleep(1)
            detail_url = 'http://www.4567kan.com'+li.xpath('./div/div/h4/a/@href').extract_first()

            # 将详情页的url存入到redis中的set
            ex = self.conn.sadd('urls',detail_url)
            if ex == 1:
                print("该url没有被爬取到，可以进行数据的爬取")
                yield scrapy.Request(url=detail_url,callback=self.parse_detail)
            else:
                print("数据无更新，暂时无新数据")

    def parse_detail(self,response):
        # sleep(0.5)
        item = MovieproItem()
        item['name'] = response.xpath('/html/body/div[1]/div/div/div/div[2]/h1/text()').extract_first()
        # print(type(item['name']))
        content = response.xpath('/html/body/div[1]/div/div/div/div[2]/p[5]/span[2]//text()').extract()
        content = ''.join(content)
        item['content'] = content
        # print(type(item['content']))

        yield item