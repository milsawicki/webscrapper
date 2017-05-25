# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
from scrapy.loader.processors import  TakeFirst

import scrapy

class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    title_pl = scrapy.Field()
    year = scrapy.Field()
    director = scrapy.Field()
    plot = scrapy.Field()
    image = scrapy.Field()
    genres = scrapy.Field()
    rate = scrapy.Field()
    pass
