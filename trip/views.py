from trip.models import Trip, Members
from trip.serializers import TripSerializer, TripMembersSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

class TripList(APIView):
	# authentication_classes = (JSONWebTokenAuthentication,)
	def get(self, request, format=None):
		trips = Trip.objects.all()
		serializer = TripSerializer(trips, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = TripSerializer(data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=HTTP_201_CREATED)
		return Response(serializer.errors, status=HTTP_404_BAD_REQUEST)

class TripMembersList(APIView):
	# authentication_classes = (JSONWebTokenAuthentication,)
	def get(self, request, trip_id, format=None):
		members = Members.objects.filter(trip_id=trip_id)
		serializer = TripMembersSerializer(members, many=True)
		return Response(serializer.data)

	def post(self, request, trip_id, format=None):
		serializer = TripMembersSerializer(data = request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=HTTP_201_CREATED)
		return Response(serializer.errors, status=HTTP_404_BAD_REQUEST)

class TripMemberDetails(APIView):
	# authentication_classes = (JSONWebTokenAuthentication,)
	def get(self, request, trip_id, user_id, format=None):
		members = Members.objects.get(trip_id=trip_id, member=user_id)
		serializer = TripMembersSerializer(members)
		return Response(serializer.data)

	def delete(self, request, trip_id, user_id, format=None):
		member = self.get(trip_id=trip_id, member=user_id)
		member.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
