import scrapy

from . import common



class Erikat2Spider(scrapy.Spider):
    name = 'erikaT2'
    allowed_domains = ['yatuu.fr']
    start_urls = []

    begURL = "1-erika-et-les-princes-en-detresse-tome-2/" # https://yatuu.fr/1-erika-et-les-princes-en-detresse-tome-2/
    endURL = "47-erika-et-les-princes-en-detresse-fin-tome-2/" # https://yatuu.fr/47-erika-et-les-princes-en-detresse-fin-tome-2/

    tDir = "Erika-T2"
    urlFile = "URListT2.txt"

    boolLogFailedRegexes = False


    def __init__(self):
        common.init(self)


    def parse(self, response):
        return common.parse(self, response)
