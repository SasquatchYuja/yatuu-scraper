import scrapy

from . import common



class Erikat1Spider(scrapy.Spider):
    name = 'erikaT1'
    allowed_domains = ['yatuu.fr']
    start_urls = []

    begURL = "erika-et-les-princes-en-detresse-page-1-a-4/" # https://yatuu.fr/erika-et-les-princes-en-detresse-page-1-a-4/
    endURL = "erika-et-les-princes-en-detresse-82/" # https://yatuu.fr/erika-et-les-princes-en-detresse-82/

    tDir = "Erika-T1"
    urlFile = "URListT1.txt"

    boolLogFailedRegexes = False # Log images' URLs that aren't downloaded because not matching the regex ?


    def __init__(self):
        common.init(self)


    def parse(self, response):
        return common.parse(self, response)
