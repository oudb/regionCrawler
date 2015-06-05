# -*- coding: utf-8 -*-
__author__ = 'odb'

from scrapy.spider import Spider
from scrapy import log
from scrapy.selector import Selector

from regionCrawler.items import Region
from utils import *

class RegionSpider(Spider):

    name = "region"
    allowed_domains = ["taobao.com"]
    start_urls = [
        "http://kezhan.trip.taobao.com/area.html",
    ]

    def parse(self, response):
        sel = Selector(response)
        rows = sel.xpath('//tbody/tr')
        current_province = None
        current_city = None
        regions = []
        for r in rows:
            cells = r.xpath('td')

            province_id = cast_to_int( extract_single_item(cells[0],'text()') )
            province_name = extract_single_item(cells[1],'text()')
            if province_id is not None and province_name is not None:
                current_province = Region()
                current_province['id'] = province_id
                current_province['name'] = province_name
                current_province['parent'] = 86
                current_province['level'] = 1
                regions.append(current_province)
                log.msg("current_province is: %s" % current_province, log.INFO)

            city_id = cast_to_int( extract_single_item(cells[2],'text()') )
            city_name = extract_single_item(cells[3],'text()')
            if city_id is not None and city_name is not None:
                current_city = Region()
                current_city['id'] = city_id
                current_city['name'] = city_name
                current_city['parent'] = current_province['id']
                current_city['level'] = 2
                regions.append(current_city)
                log.msg("current_city is: %s" % current_city, log.INFO)

            area_id = cast_to_int( extract_single_item(cells[4],'text()') )
            area_name = extract_single_item(cells[5],'text()')
            if area_id is not None and area_name is not None:
                area = Region()
                area['id'] = area_id
                area['name'] = area_name
                area['parent'] = current_city['id']
                area['level'] = 3
                regions.append(area)

        return regions