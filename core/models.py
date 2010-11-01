# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Author( models.Model ):
	login = models.CharField( _( "login" ), max_length=255 )
	
	class Meta:
		verbose_name = _( "Author" )
		verbose_name_plural = _( "Authors" )

	def __str__( self ):
		return self.login


class Image( models.Model ):
	author = models.ForeignKey( Author, verbose_name=_( "author" ) )
	url = models.CharField( _( "url" ), max_length=255 )
	image = models.ImageField( _( "image" ), upload_to='images' )

	class Meta:
		verbose_name = _( "Image" )
		verbose_name_plural = _( "Images" )

	def __str__( self ):
		return self.url

# vim: fdm=marker ts=4 sw=4 sts=4

