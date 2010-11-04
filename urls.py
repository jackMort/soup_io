import os

from django.conf.urls.defaults import *
from django.contrib import admin
from soup_io.core.views import index, by_author, download

admin.autodiscover()

urlpatterns = patterns(
	'',
	url( r'^admin/', include( admin.site.urls ) ),
    url( r'^media/(.*)$', 'django.views.static.serve', { 'document_root' : os.path.join( os.path.dirname( __file__ ), 'media' ) } ),
	
	url( r'^$', index ),
	url( r'^(?P<author>[\w\-]+)/$', by_author ),
	url( r'^(?P<author>[\w\-]+)/download$', download ),

)
