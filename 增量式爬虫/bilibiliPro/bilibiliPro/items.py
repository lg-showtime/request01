# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BilibiliproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    video_url = scrapy.Field()
    video_name = scrapy.Field()
    up_name = scrapy.Field()
    video_playnum = scrapy.Field()
