import scrapy


class BossSpider(scrapy.Spider):
    name = 'boss'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.zhipin.com/job_detail/?query=python&city=100010000&industry=&position=']

    def parse(self, response):
        li_list = response.xpath('//*[@id="main"]/div/div[2]/ul/li')
        for li in li_list:
            job_name = li.xpath('.//div[@class="job-title"]/span/text()').extract_first()
            print(job_name)
