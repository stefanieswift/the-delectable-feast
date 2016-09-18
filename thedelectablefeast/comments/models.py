from __future__ import unicode_literals

from django.db import models
from users.models import Users
from recipes.models import Recipes


class Comment(models.Model):
	recipe = models.ForeignKey(Recipes)
	created = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(Users)
	foodBlogAdvice = models.PositiveSmallIntegerField()
	rating = models.PositiveSmallIntegerField()
	comment = models.TextField()

	class Admin:
		pass


class Response(models.Model):
	comment = models.ForeignKey(Comment)
	response = models.TextField()
	user = models.ForeignKey(Users)

	class Admin:
		pass

