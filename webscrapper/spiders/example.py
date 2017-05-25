# -*- coding: utf-8 -*-
import scrapy
import  re
from webscrapper.items import MovieItem


class QuotesSpider(scrapy.Spider):
    name = "topFilms"
    allowed_domains = ["filmweb.pl"]

    def start_requests(self):
        urls = [
            'http://www.filmweb.pl/search/serial',
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        index = 0
        for position in response.css('.filmPreview '):
            item = MovieItem()
            item['title'] = position.css('.filmTitle::text').extract_first()
            item['title_pl'] = position.css('.filmTitle::text').extract_first()
            item['year'] = position.css('span[class=filmYear]::text').extract_first()
            item['plot'] = position.css('.filmPlot p::text').extract_first()
            item['director'] = position.css('.filmInfo a[target=_blank]::text').extract_first()
            item['image'] = position.css('img::attr(src)').extract()[1]
            item['genres'] = position.css('.filmGenres a[href]::text').extract()
            item['rate'] = response.css('script[data-type=setfilm]').re(r'\d.\d')[index]
            index +=1
            yield item

        next_page = response.xpath('//*[@class="nextLink"]//@href').extract()
        if next_page:
            next_href = next_page[0]
            next_page_url = 'http://www.filmweb.pl/search/serial' + next_href
            request = scrapy.Request(url=next_page_url)
            yield request
