# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BadvSpiderItem(scrapy.Item):
    name = scrapy.Field()
    company = scrapy.Field()
    style = scrapy.Field()
    country = scrapy.Field()
    state = scrapy.Field()
    image_url = scrapy.Field()
    score = scrapy.Field()
