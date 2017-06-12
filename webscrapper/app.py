# server.py
import json

from klein import route, run
from scrapy import signals
from scrapy.crawler import CrawlerRunner
from spiders.ListSpider import ListSpider
from spiders.PositionSpider import PositionSpider

class MyCrawlerRunner(CrawlerRunner):

    def crawl(self, crawler_or_spidercls, *args, **kwargs):
        self.items = []
        crawler = self.create_crawler(crawler_or_spidercls)
        crawler.signals.connect(self.item_scraped, signals.item_scraped)
        dfd = self._crawl(crawler, *args, **kwargs)
        dfd.addCallback(self.return_items)
        return dfd

    def item_scraped(self, item, response, spider):
        self.items.append(item)

    def return_items(self, result):
        return self.items

def return_spider_output(output):
    return json.dumps([dict(item) for item in output])

@route("/search/<query>")
def search(request, query):
    runner = MyCrawlerRunner()
    deferred = runner.crawl(ListSpider, query = query)
    deferred.addCallback(return_spider_output)
    return deferred

@route("/title/<id>")
def getmovie(request, id, ):
    runner = MyCrawlerRunner()
    deferred = runner.crawl(PositionSpider, id = id)
    deferred.addCallback(return_spider_output)
    return deferred

run("localhost", 8080)
