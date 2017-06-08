
BOT_NAME = 'webscrapper'
SPIDER_MODULES = ['webscrapper.spiders']
NEWSPIDER_MODULE = 'webscrapper.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'webscrapper.pipelines.FilmwebPipeline': 300,
}

# SPIDER_SETTINGS = [
#     {
#         'endpoint': 'topFilms',
#         'location': 'spiders.FilmSpider',
#         'spider': 'FilmSpider',
#         'scrapy_settings': {
#             'ITEM_PIPELINES': {
#                 'pipelines.AddTablePipeline': 500
#             }
#         }
#     }
# ]

FEED_EXPORT_ENCODING = {
    'json': 'utf-8',
}
#
#
# MONGODB_HOST = "localhost"
# MONGODB_PORT = 27017
# MONGODB_DB = "filmweb_base"
# MONGODB_COLLECTION = "movies"