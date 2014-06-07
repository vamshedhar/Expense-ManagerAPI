from rest_framework import serializers
from users.models import UserDetail

class UsersSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserDetail
		fields = ('user_id', 'first_name', 'last_name', 'contact', 'balance')