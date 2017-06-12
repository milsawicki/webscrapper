# -*- coding: utf-8 -*-
import scrapy
from items import ListItem
from items import MovieItem
class ListSpider(scrapy.Spider):
    name = 'seriesSpider'
    def start_requests(self):
        yield scrapy.Request('http://www.imdb.com/find?q=%s&s=tt&exact=true&ref_=fn_tt_ex' % self.query)

    def parse(self, response):
        for pos in response.css('.findResult'):
            item = ListItem()
            item['title'] = pos.css('.result_text a::text').extract_first()
            item['id'] = pos.css('.findResult .result_text a::attr(href)').extract()[0].split('/')[2]
            item['year'] = pos.css('.result_text::text').re('\d+')[0]
            yield item
