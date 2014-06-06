from django.db import models

class Users(models.Model):
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=200)
	firstName = models.CharField(max_length=100)
	lastName = models.CharField(max_length=100)
	email = models.EmailField(max_length=254)
	contact = models.BigIntegerField()
	balance = models.IntegerField(default=0)
	timestamp = models.DateTimeField(auto_now_add=True)