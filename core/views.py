from django.conf import settings
from django.http import HttpResponse
from django.template import RequestContext
from django.core.servers.basehttp import FileWrapper
from django.shortcuts import render_to_response, get_object_or_404

import tempfile, zipfile, os

from soup_io.core.models import Author, Image, Post

def index( request ):
	images = Image.objects.all()
	graph = request.GET.get( 'graph', 'false' )

	if request.is_ajax():
		template = "images_part.html"
	else:
		if graph == 'true':
			template = "graph.html"
		else:
			template = "images.html"

	return render_to_response(
		template, { "images": images }, context_instance = RequestContext( request )
	)

def by_author( request, author ):
	author = get_object_or_404( Author, login=author )
	images = Post.objects.filter( author=author )
	graph = request.GET.get( 'graph', 'false' )
	
	if request.is_ajax():
		template = "images_part.html"
	else:
		if graph == 'true':
			template = "graph.html"
		else:
			template = "images.html"

	return render_to_response(
		template, { "post": True, "author": author, "images": images }, context_instance = RequestContext( request )
	)

def user_list( request ):
	users = Author.objects.filter( virtual=False )

	return render_to_response(
		"users.html", { "users": users }, context_instance = RequestContext( request )
	)


def download( request, author ):
	author = get_object_or_404( Author, login=author )
	posts = Post.objects.filter( author=author )
	
	temp = tempfile.TemporaryFile()
	archive = zipfile.ZipFile( temp, 'w', zipfile.ZIP_DEFLATED )
	for post in posts:
		archive.write( "%s%s" % ( settings.HOME_DIR, post.image.image.url ), post.image.image.url.replace( "/media/images/full/", "" ) )
	archive.close()

	wrapper = FileWrapper( temp )
	response = HttpResponse( wrapper, content_type='application/zip' )
	response['Content-Disposition'] = 'attachment; filename=%s.zip' % author
	response['Content-Length'] = temp.tell()
	temp.seek( 0 )

	return response
