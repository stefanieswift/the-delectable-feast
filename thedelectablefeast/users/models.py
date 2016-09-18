from __future__ import unicode_literals

from django.db import models
import time


class Users(models.Model):
	email = models.CharField(max_length=255)
	name = models.CharField(max_length=255)
	joined = models.DateTimeField(auto_now_add=True)
	subscriber = models.PositiveSmallIntegerField()

	class Admin:
		pass


class Bios(models.Model):
	user = models.ForeignKey(Users)
	bio = models.TextField()

	class Admin:
		pass


class Roles(models.Model):
	role = models.CharField(max_length=60)

	class Admin:
		pass


class Rights(models.Model):
	role = models.ForeignKey(Roles)
	user = models.ForeignKey(Users)

	class Admin:
		pass
