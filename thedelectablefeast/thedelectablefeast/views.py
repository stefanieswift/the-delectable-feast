from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Template, Context
from django.shortcuts import render_to_response


def about(request):
	return render_to_response('about/about.html', {})


def about_author(request, offset):
	return render_to_response('about/aboutTheAuthor.html',
	{
		'author': str(offset)
	})
