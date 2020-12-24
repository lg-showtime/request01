# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from scrapy.http import HtmlResponse
from time import sleep
class BilibiliproDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        bro = spider.bro
        bro.get(request.url)
        sleep(2)
        all_window_height = []
        all_window_height.append(bro.execute_script("return document.body.scrollHeight;"))
        while True:
            bro.execute_script("scroll(0,100000)")
            sleep(1)
            check_height = bro.execute_script("return document.body.scrollHeight;")
            if check_height == all_window_height[-1]:
                # bro.execute_script("scroll(0,document.body.scrollHeight)")
                print("我已下拉完毕")
                break
            else:
                all_window_height.append(check_height)
                print("我正在下拉")


        page_text = bro.page_source
        new_response = HtmlResponse(url=request.url, body=page_text, encoding='utf-8', request=request)
        return new_response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass
