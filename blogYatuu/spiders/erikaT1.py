import scrapy

from . import common



class Erikat1Spider(scrapy.Spider):
    name = 'erikaT1'
    allowed_domains = ['yatuu.fr']
    start_urls = []

    begURL = "erika-et-les-princes-en-detresse-page-1-a-4/" # https://yatuu.fr/erika-et-les-princes-en-detresse-page-1-a-4/
    endURL = "erika-et-les-princes-en-detresse-82/" # https://yatuu.fr/erika-et-les-princes-en-detresse-82/
    #begURL = "erika-princes-detresse-67/"
    #endURL = "erika-princes-detresse-67/"

    def parse(self, response):
        pass
