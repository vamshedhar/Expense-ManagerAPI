from django.db import models
from django.conf import settings
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class UserManager(BaseUserManager):
	def save_user(self, email, password, is_staff, is_superuser):
		email = self.normalize_email(email)
		user = self.model(email=email, is_staff=is_staff, is_superuser=is_superuser, is_active=True)
		user.set_password(password)
		user.save()
		return user

	def create_user(self, email, password):
		return self.save_user(email, password, False, False)

	def create_superuser(self, email, password):
		return self.save_user(email, password, True, True)


class User(AbstractBaseUser, PermissionsMixin):
	"""
	Custom user model for the application which uses email as the username 
	"""
	email = models.EmailField(max_length=254, unique=True)
	first_name = models.CharField(max_length=30, blank=True)
	last_name = models.CharField(max_length=30, blank=True)
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	date_joined = models.DateTimeField(auto_now_add=True)

	objects = UserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	def get_full_name(self):
		"""
		Returns the first_name plus the last_name, with a space in between.
		"""
		full_name = '%s %s' % (self.first_name, self.last_name)
		return full_name.strip()

	def get_short_name(self):
		"Returns the short name for the user."
		return self.first_name

class UserDetail(models.Model):
	"""
	Personal details of user related to the application
	"""
	user_id = models.ForeignKey(settings.AUTH_USER_MODEL)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	contact = models.BigIntegerField()
	balance = models.IntegerField(default=0)