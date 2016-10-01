from django.db.models import Q
from django.http import Http404
from django.http import HttpResponseRedirect
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
	return render_to_response('submit_recipe.html', {'form': form})


def feed(request):
	recipes = Recipes.objects.all()[:15]
	return render_to_response('recipe_feed.html', {'recipes' : recipes})


def view_recipes(request, recipe_info):
	recipe_info = recipe_info.split("/")
	recipe_id = recipe_info[0]
	recipe = Recipes.objects.filter(id=recipe_id).distinct()[0]

	if not recipe:
		if len(recipe_info) > 1:
			recipe = Recipes.object.filter(title=recipe_info[1])
			if not recipe:
				return Http404
	if len(recipe_info) < 2 or recipe_info[1] != recipe.title:
		recipe_url = Recipes.SITE_URL + recipe_id + "/" + recipe.title + "/"
		return HttpResponseRedirect(recipe_url)
	return render_to_response('view_recipe.html', {
		'recipe' : recipe
	})