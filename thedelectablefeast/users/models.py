from __future__ import unicode_literals

from django.db import models


class Users(models.Model):
	email = models.CharField(max_length=255)
	name = models.CharField(max_length=255)
	joined = models.DateTimeField(auto_now_add=True)
	subscriber = models.PositiveSmallIntegerField()

	class Admin:
		pass