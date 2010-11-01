import hashlib

from scrapy.conf import settings as scrapy_settings
from scrapy.contrib.pipeline.images import ImagesPipeline
from soup_io.core.models import Author, Image

class SoupImages( ImagesPipeline ):
	def image_key(self, url):
		image_guid = hashlib.sha1(url).hexdigest()
		return 'full/%s.%s' % ( image_guid, url.split( ".")[-1] )

class SoupPipeline( object ):

	def process_item(self, item, spider):
		
		author, created = Author.objects.get_or_create( login=scrapy_settings.get( 'LOGIN' ) )
		image = item['images'][0]

		try:
			image = Image.objects.get( url=image['url'] )
		except Image.DoesNotExist:
			image = Image.objects.create( author=author, url=image['url'], image="images/%s" % ( image['path'] ) )

		return item
