# Scrapy settings for regionCrawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'regionCrawler'

SPIDER_MODULES = ['regionCrawler.spiders']
NEWSPIDER_MODULE = 'regionCrawler.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'regionCrawler (+http://www.yourdomain.com)'


#odb
MYSQL_HOST = "103.244.235.2"
MYSQL_USER = "luckycat"
MYSQL_PASSWD = "9zctv8qWjzRvPxhY"
MYSQL_DB = "luckycat"
MYSQL_CHARSER = "utf8"

ITEM_PIPELINES = {
    'regionCrawler.pipelines.UpdateRegion': 1,
}