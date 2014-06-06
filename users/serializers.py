from rest_framework import serializers
from users.models import User

# class UsersSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Users
# 		fields = ('id', 'username', 'password', 'firstName', 'lastName', 'email', 'contact', 'balance', 'timestamp')