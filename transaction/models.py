from django.db import models
from trip.models import Trip
from django.conf import settings

class Transaction(models.Model):
	description = models.TextField()
	amount = models.IntegerField()
	trip = models.ForeignKey(Trip)
	member = models.ForeignKey(settings.AUTH_USER_MODEL)
	created_time = models.DateTimeField(auto_now=True)