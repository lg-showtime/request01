import scrapy


class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua'
    # allowed_domains = ['www.xx.com']
    start_urls = ['http://www.521609.com/meinvxiaohua/']

    url='http://www.521609.com/meinvxiaohua/list12%d.html'
    page_num = 2
    def parse(self, response):
        li_list = response.xpath('//*[@id="content"]/div[2]/div[2]/ul/li')
        print("正在爬取第{}页.........".format(self.page_num))
        for li in li_list:
            img_name = li.xpath('./a[2]/text() | ./a[2]/b/text()').extract_first()
            print(img_name)

        if self.page_num <= 11:
            new_url = format(self.url%self.page_num)
            self.page_num += 1

            # 手动请求发送：callback 回调函数是专门用作与数据解析的
            yield scrapy.Request(url=new_url,callback=self.parse)