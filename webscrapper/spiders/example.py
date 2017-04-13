# -*- coding: utf-8 -*-
import scrapy
from webscrapper.items import MovieItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class QuotesSpider(scrapy.Spider):
    name = "topFilms"
    allowed_domains = ["filmweb.pl"]

    def start_requests(self):
        urls = [
            'http://www.filmweb.pl/search/serial',
        ]
        rules = (Rule(LinkExtractor(allow=(), restrict_xpaths=('//a[@class="button next"]',)), callback="parse_page",
                      follow=True),)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        for position in response.css('.filmContent '):
            item = MovieItem()
            item['title'] = position.css('.filmSubtitle::text').extract_first()
            item['title_pl'] = position.css('.filmTitle::text').extract_first()
            item['year'] = position.css('.infoYear::text').extract_first()
            # item['plot'] = position.css('.filmPlot::text').extract_first()
            yield item

        next_page = response.xpath('//*[@class="nextLink"]//@href').extract()
        if next_page:
            next_href = next_page[0]
            next_page_url = 'http://www.filmweb.pl/search/serial' + next_href
            request = scrapy.Request(url=next_page_url)
            yield request
