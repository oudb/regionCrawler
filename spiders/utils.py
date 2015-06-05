# -*- coding: utf-8 -*-
__author__ = 'odb'


def extract_single_item(item, path):
        items = item.xpath(path).extract()
        res = ''.join(items).strip()
        return res if res != '' else None
def re_single_item(item, path, rex ):
        items = item.xpath(path).re(rex)
        res = ''.join(items).strip()
        return res if res != '' else None

def cast_to_float(num_str):
    if num_str is None:
        return num_str
    try:
        return float(num_str)
    except ValueError:
        return None

def cast_to_int(num_str):
    if num_str is None:
        return num_str
    try:
        return int(num_str)
    except ValueError:
        return None


