# Jaziel Lopez <juan.jaziel@gmail.com>
# Software Developer
# http://jlopez.mx

import scrapy

from items.olympic import OlympicItem


class BootSpider(scrapy.Spider):
    name = 'boot'
    allowed_domains = []  # ["olympictech.org"]
    start_urls = []  # ["http://odf.olympictech.org/2016-Rio/rio_2016_OG.htm"]

    def parse(self, response):
        for sel in response.xpath('//tbody/tr[22]/td[5]'):
            item = OlympicItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['abstract'] = sel.xpath('a/@data').extract()
            yield item
