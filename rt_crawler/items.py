# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RTItem(scrapy.Item):
    title = scrapy.Field()
    score = scrapy.Field()
    genres = scrapy.Field()
    consensus = scrapy.Field()
