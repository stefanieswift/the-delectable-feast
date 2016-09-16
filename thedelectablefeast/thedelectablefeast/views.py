from django.http import HttpResponse


def about(request):
	pamela = "Pamela is a great chef. "
	stefanie = " Stefanie is learning"
	html = pamela + stefanie
	return HttpResponse(html)


def about_author(request, offset):
	author = str(offset)
	author_bio = author + " is fantastically epic."
	html = author_bio
	return HttpResponse(html)
