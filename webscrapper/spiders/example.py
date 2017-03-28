# -*- coding: utf-8 -*-
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "films"

    def start_requests(self):
        urls = [
            'http://www.filmweb.pl/rankings/film/world',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for position in response.css('td.place a.s-20::text'):
            yield {
                'title': position.extract(),
            }
