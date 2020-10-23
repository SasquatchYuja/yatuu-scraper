import scrapy

from . import common



class Erikat1Spider(scrapy.Spider):
    name = 'erikaT1'
    allowed_domains = ['yatuu.fr']
    start_urls = []


    def parse(self, response):
        pass
