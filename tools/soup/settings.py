# Scrapy settings for soup project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
# Or you can copy and paste them from where they're defined in Scrapy:
# 
#     scrapy/conf/default_settings.py
#
import os

from django.conf import settings

BOT_NAME = 'soup'
BOT_VERSION = '1.0'

ITEM_PIPELINES = [ 'soup.pipelines.SoupImages','soup.pipelines.SoupPipeline'  ]

IMAGES_STORE= os.path.join( settings.MEDIA_ROOT, 'images' )


SPIDER_MODULES = ['soup.spiders']
NEWSPIDER_MODULE = 'soup.spiders'
DEFAULT_ITEM_CLASS = 'soup.items.SoupItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

