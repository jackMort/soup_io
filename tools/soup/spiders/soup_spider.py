import re

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
	
	stop_flag = False
	def stop( self ):
		self.stop_flag = True

	def parse( self, response ):
		if self.stop_flag: return
		
		hxs = HtmlXPathSelector( response )

		posts = hxs.select( '//div[contains(@class, "post")]' )
		for post in posts:
			id = post.select( '@id' ).extract()
			if id:
				id = int( id[0].replace( 'post', '' ) )
				imagecontainer = post.select( './/div[@class="content-container"]/div[@class="content "]/div[@class="imagecontainer"]')
				# if type = image
				if imagecontainer:

					item = SoupItem()
					item['id'] = id
					
					image_url = imagecontainer.select( './/a/img/@src' ).extract()
					if len( image_url ) == 0:
						image_url = imagecontainer.select( './/img/@src' ).extract()
					
					image_url = image_url[0]
					if re.match( "http://(.*)/(.*)/(\d+)/(.*)_(.*)_(\d+)\.(.*)", image_url ):
						image_url = re.sub( r'_(\d+)\.', '.', image_url )
					
					item['image_urls'] = [ image_url ]

					source = post.select( './/div[contains(@class, "source")]' )
					if source:
						text = source.select( 'text() ').extract()
						authors = source.select( './/span/a/img/@title' ).extract()
						if text and 'Reposted from' in text[0]:
							item['reposted_from'] = authors[0]
							if len( text ) > 1 and 'via' in text[1]:
								item['via'] = authors[1]

					yield item

		more = hxs.select( '//a[@name="more"]/@href' ).extract()
		if len( more ) == 1:
			yield Request( "http://%s.soup.io%s" % ( self.login, more[0] ), callback=self.parse )
