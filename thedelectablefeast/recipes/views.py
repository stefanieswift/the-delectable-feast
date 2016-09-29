from django.db.models import Q
from django.shortcuts import render_to_response
from forms import ContactForm
from models import Recipes


def search(request):
	query = request.GET.get('recipes', '')
	results = []
	if query:
		qset = (
			Q(title__icontains=query) |
			Q(authors__first_name__icontains=query) |
			Q(authors__last_name__icontains=query)
		)
		results = Recipes.objects.filter(qset).distinct()
	return render_to_response("search.html", {
		"results": results,
		"query": query
	})


def submit(request):
	form = ContactForm()
	return render_to_response('submitRecipe.html', {'form': form})


def feed(request):
	recipes = Recipes.objects.all()[:15]
	return render_to_response('recipeFeed.html', {'recipes' : recipes})


