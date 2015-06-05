# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
from scrapy import log

from settings import MYSQL_HOST,MYSQL_USER,MYSQL_PASSWD,MYSQL_DB,MYSQL_CHARSER

class UpdateRegion(object):
    def __init__(self):
        self.conn  = MySQLdb.connect(host=MYSQL_HOST,user=MYSQL_USER,passwd=MYSQL_PASSWD,db=MYSQL_DB,charset=MYSQL_CHARSER )
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            self.cursor.execute("INSERT INTO zy_region (region_id, region_name, parent_id, level) VALUES(%s, %s, %s, %s)",
                                (item["id"],item["name"],item["parent"],item["level"]) )
            self.conn.commit()
        except MySQLdb.IntegrityError,ie:
            try:
                log.msg("UpdateRegion-IntegrityError %d: %s" % (ie.args[0], ie.args[1]), log.DEBUG )
                self.cursor.execute("UPDATE zy_region SET region_name=%s, parent_id=%s, level=%s WHERE region_id=%s",
                                    (item["name"],item["parent"],item["level"], item["id"])
                )
                self.conn.commit()
            except MySQLdb.Error,e:
                log.msg("UpdateRegion-Error %d: %s--%s" % (e.args[0], e.args[1],item), log.ERROR )
        except MySQLdb.Error, e:
            log.msg("UpdateRegion-Error %d: %s--%s" % (e.args[0], e.args[1],item), log.ERROR )

        return item
