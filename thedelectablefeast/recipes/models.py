from __future__ import unicode_literals

from django.db import models
from users.models import Users


class Recipes(models.Model):
	title = models.CharField(max_length=60)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now_add=True)
	thumbnail = models.CharField(max_length=60)

	class Admin:
		pass


class Post(models.Model):
	recipe = models.ForeignKey(Recipes)
	body = models.TextField()
	metaDescription = models.CharField(max_length=160)

	class Admin:
		pass


class Author(models.Model):
	recipe = models.ForeignKey(Recipes)
	author = models.ForeignKey(Users)


class Videos(models.Model):
	recipe = models.ForeignKey(Recipes)
	url = models.CharField(max_length=255)
	primary_video = models.PositiveSmallIntegerField()


class Rating(models.Model):
	recipe = models.ForeignKey(Recipes)
	user = models.ForeignKey(Users)


class Tags(models.Model):
	tag = models.CharField(max_length=155)
	masterTag = models.PositiveSmallIntegerField(default=0)


class TagAssociations(models.Model):
	recipe = models.ForeignKey(Recipes)
	tag = models.ForeignKey(Tags)





