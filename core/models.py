# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Author( models.Model ):
	login = models.CharField( _( "login" ), max_length=255 )
	virtual = models.BooleanField( _( "virtual" ), default=1 )
	posts = models.ManyToManyField( "Post", null=True, blank=True )
	
	class Meta:
		verbose_name = _( "Author" )
		verbose_name_plural = _( "Authors" )

	def __str__( self ):
		return self.login

class Image( models.Model ):
	author = models.ForeignKey( Author, verbose_name=_( "author" ), related_name="image_author" )
	url = models.CharField( _( "url" ), max_length=255 )
	image = models.ImageField( _( "image" ), upload_to='images' )

	class Meta:
		verbose_name = _( "Image" )
		verbose_name_plural = _( "Images" )
		ordering = [ "-id" ]

	def __str__( self ):
		return self.url


class Post( models.Model ):
	image = models.ForeignKey( Image )
	via = models.ForeignKey( Author, blank=True, null=True )
	original_id = models.IntegerField()
	
	class Meta:
		verbose_name = _( "Post" )
		verbose_name_plural = _( "Posts" )
		ordering = [ "-original_id" ]

# vim: fdm=marker ts=4 sw=4 sts=4
