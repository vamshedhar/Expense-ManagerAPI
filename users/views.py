# from users.models import User
# from users.serializers import UsersSerializer
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# class UsersList(APIView):
# 	"""
# 	List of all users
# 	"""

# 	def get(self, request, format=None):
# 		users = User.objects.all()
# 		serializer = UsersSerializer(users, many=True)
# 		return Response(serializer.data)

# 	def post(self, request, format=None):
# 		serializer = UsersSerializer(data.request.DATA)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=HTTP_201_CREATED)
# 		return Response(serializer.errors, status=HTTP_404_BAD_REQUEST)

# class UserDetails(APIView):
# 	"""
# 	Specific user details 
# 	"""
# 	def get_user(self, pk):
# 		try:
# 			return Users.objects.get(pk=pk)
# 		except Users.DoesNotExist:
# 			raise Http404

# 	def get(self, request, pk, format=None):
# 		user = self.get_user(pk)
# 		serializer = UsersSerializer(user)
# 		return Response(serializer.data)

# 	def put(self, request, pk, format=None):
# 		user = self.get_user(pk)
# 		serializer = UsersSerializer(user, data=request.DATA)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)