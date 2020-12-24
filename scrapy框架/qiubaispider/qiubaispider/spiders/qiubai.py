import scrapy
from qiubaispider.items import QiubaispiderItem

class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    # def parse(self, response):
    #     # 解析 作者的名称+段子内容
    #     div_list = response.xpath('//div[@id="content"]/div/div[2]/div')
    #     div_data = []
    #     for div in div_list:
    #         # xpath 返回的是列表，但是列表元素一定是Selector类型的对像
    #         # extract可以将Selector 对象中data参数存储的字符串提取出来
    #         author_name = div.xpath('./div/a[2]/h2/text()')[0].extract()
    #         # author_name = div.xpath('./div/a[2]/h2/text()').extract_first()
    #         # 列表调用了extract 之后，则表示将列表中每一个Selector对象中的data对应的字符串提取出来
    #         content = div.xpath('./a[1]/div/span//text()').extract()
    #         content = ''.join(content)
    #         # print(author_name,content)
    #         dic = {
    #             'author':author_name,
    #             'content':content
    #         }
    #         div_data.append(dic)
    #     return div_data
    def parse(self, response):
        # 解析 作者的名称+段子内容
        div_list = response.xpath('//div[@id="content"]/div/div[2]/div')
        div_data = []
        for div in div_list:
            # xpath 返回的是列表，但是列表元素一定是Selector类型的对像
            # extract可以将Selector 对象中data参数存储的字符串提取出来
            author_name = div.xpath('./div/a[2]/h2/text() | ./div[1]/span/h2/text()')[0].extract()
            # author_name = div.xpath('./div/a[2]/h2/text()').extract_first()
            # 列表调用了extract 之后，则表示将列表中每一个Selector对象中的data对应的字符串提取出来
            content = div.xpath('./a[1]/div/span//text()').extract()
            content = ''.join(content)

            item = QiubaispiderItem()
            print(type(item))
            item['author_name'] = author_name
            item['content'] = content

            # 将item提交给管道
            yield item
