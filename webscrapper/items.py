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
    plot = scrapy.Field()
    year = scrapy.Field()
    poster = scrapy.Field()
    director = scrapy.Field()
    rating = scrapy.Field()
    genres = scrapy.Field()
    pass

class ListItem(scrapy.Item):
    title = scrapy.Field()
    id = scrapy.Field()
    year = scrapy.Field()