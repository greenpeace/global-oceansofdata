# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.item import Item, Field

import re, json

f = open('data.jsonlines', 'w');

class NdbcSpider(CrawlSpider):
    name = "ndbc"
    allowed_domains = ["ndbc.noaa.gov"]
    start_urls = ['http://www.ndbc.noaa.gov/to_station.shtml']
    rules = [
        Rule(SgmlLinkExtractor(allow=r"^.+station", unique=True), callback='parse_item')
    ]

    def parse_item(self, response):
        sel = Selector(response)
        rss = sel.xpath('//link[contains(@title,"near")]/@href')[0].extract()

        m = re.search(r"lat=(.+[NS]).+lon=(.+[EW])", rss)
        d = {}
        if m:
            lat, lon = m.groups()
            d['lat'] = lat
            d['lon'] = lon

        d['rss'] = rss
        d['source'] = response.url

        f.write("%s\n" % json.dumps(d));
        pass
