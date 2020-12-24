# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy
from scrapy.pipelines.images import ImagesPipeline
# class CountrygeogspiderPipeline:
#     def process_item(self, item, spider):
#         return item
class ImgPipeLine(ImagesPipeline):
    # 对item中的图片进行请求操作
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['img_final_src'])

    # 定制图片的名称
    def file_path(self, request, response=None, info=None):
        url = request.url
        name = url.split('/')[-1]
        file_name = name.split('@')[0]
        print(file_name)
        return file_name

    def item_completed(self, results, item, info):
        return item  # 该返回值会传递给下一个即将被执行的管道类

