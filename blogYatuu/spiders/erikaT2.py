import scrapy

from . import common



class Erikat2Spider(scrapy.Spider):
    name = 'erikaT2'
    allowed_domains = ['yatuu.fr']
    start_urls = []


    def parse(self, response):
        pass
