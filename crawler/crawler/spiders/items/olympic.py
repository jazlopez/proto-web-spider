# Jaziel Lopez <juan.jaziel@gmail.com>
# Software Developer
# http://jlopez.mx

import scrapy


class OlympicItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    link = scrapy.Field()
    abstract = scrapy.Field()
