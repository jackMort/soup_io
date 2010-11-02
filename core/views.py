from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
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
