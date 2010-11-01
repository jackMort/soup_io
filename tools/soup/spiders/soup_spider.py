from scrapy.conf import settings
from scrapy.spider import BaseSpider
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector

from soup.items import SoupItem

class SoupSpider( BaseSpider ):
	name = "soup.io"
	login = settings.get( 'LOGIN' )
	allowed_domains = [ "soup.io" ]
	start_urls = [
		"http://%s.soup.io" % login,
	]

	def parse( self, response ):
		hxs = HtmlXPathSelector( response )
		images = hxs.select( '//div[@class="content "]/div[@class="imagecontainer"]/a/img/@src' ).extract()

		for image in images:
			item = SoupItem()
			item['image_urls'] = [image]

			yield item

		more = hxs.select( '//a[@name="more"]/@href' ).extract()
		print "images:", images, "next:", more

		if len( more ) == 1:
			yield Request( "http://%s.soup.io%s" % ( self.login, more[0] ), callback=self.parse )
