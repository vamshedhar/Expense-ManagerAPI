from rest_framework import serializers
from trip.models import Trip, Members

class TripSerializer(serializers.ModelSerializer):
	class Meta:
		model = Trip
		fields = ('id', 'name', 'description', 'total_members', 'expenses', 'is_open', 'admin')

class TripMembersSerializer(serializers.ModelSerializer):
	class Meta:
		model = Members
		fields = ('id', 'member', 'trip_id')

class TripMemberDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Members
		fields = ('id', 'member', 'trip_id')