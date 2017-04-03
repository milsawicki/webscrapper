# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from webscrapper.items import MovieItem
from scrapy.contrib.loader.processor import TakeFirst

class QuotesSpider(scrapy.Spider):
    name = "topFilms"
    allowed_domains = ["filmweb.pl"]

    def start_requests(self):
        urls = [
            'http://www.filmweb.pl/rankings/film/world',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        index =0;
        for position in response.css('.element'):
            item = MovieItem()
            item['title'] = position.css('.cap::text').extract_first()
            item['title_pl'] = position.css('.s-20::text').extract_first()
            item['rating'] = position.css('.s-16::text').extract_first()
            yield item