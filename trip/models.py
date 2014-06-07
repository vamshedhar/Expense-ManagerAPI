from django.db import models
from django.conf import settings

class Trip(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	total_members = models.IntegerField(default=1)
	expenses = models.IntegerField(default=0)
	is_open = models.BooleanField(default=True)
	admin = models.ForeignKey(settings.AUTH_USER_MODEL)

class Members(models.Model):
	member = models.ForeignKey(settings.AUTH_USER_MODEL)
	trip_id = models.ForeignKey(Trip)