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
            'http://www.filmweb.pl/search/serial?q=&type=&startYear=&endYear=&countryIds=&genreIds=&startRate=&endRate=&startCount=1000&endCount=&sort=COUNT&sortAscending=false&c=portal&page=1',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse_page(self, response):
        index =1;
        for position in response.css('.filmPreview '):
            item = MovieItem()
            item['title'] = position.css('.filmSubtitle::text').extract_first()
            item['title_pl'] = position.css('.filmTitle::text').extract_first()
            item['year'] = position.css('.infoYear::text').extract_first()
            item['plot'] = position.css('.filmPlot::text').extract_first()
            yield item