from django.contrib import admin
from users.models import User, UserDetail

admin.site.register(User)
admin.site.register(UserDetail)