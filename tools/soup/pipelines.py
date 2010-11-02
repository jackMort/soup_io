import hashlib

from scrapy.conf import settings as scrapy_settings
from scrapy.contrib.pipeline.images import ImagesPipeline
from soup_io.core.models import Author, Image, Post

class SoupImages( ImagesPipeline ):
	def image_key(self, url):
		image_guid = hashlib.sha1(url).hexdigest()
		return 'full/%s.%s' % ( image_guid, url.split( ".")[-1] )

class SoupPipeline( object ):

	def process_item(self, item, spider):
		via = None

		user, created = Author.objects.get_or_create( login=scrapy_settings.get( 'LOGIN' ) )
		if item['reposted_from']:
			author, created = Author.objects.get_or_create( login=item['reposted_from'] )
			if item['via']:
				via, created = Author.objects.get_or_create( login=item['via'] )
		else:
			author = user

		image = item['images'][0]

		try:
			image = Image.objects.get( url=image['url'] )
			print "image: %s already exists linking !" % image.url
		except Image.DoesNotExist:
			image = Image.objects.create( author=author, url=image['url'], image="images/%s" % ( image['path'] ) )
		
		try:
			post = Post.objects.get( original_id=item['id'] )
			print " -- Post %s already exists ..."
		except Post.DoesNotExist:
			post = Post( image=image, via=via, original_id=item['id'] )
			post.save()

			user.posts.add( post )
			user.save()

		return item
