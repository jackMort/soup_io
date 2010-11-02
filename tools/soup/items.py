# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class SoupItem(Item):
	id = Field()
	images = Field()
	image_urls = Field()
	reposted_from = Field( default=None )
	via = Field( default=None )
