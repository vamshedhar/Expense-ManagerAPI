from transaction.models import Transaction
from transaction.serializers import TransactionListSerializer, TripTransactionsSerializer, TransactionDetailsSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

class TransactionList(APIView):
	# authentication_classes = (JSONWebTokenAuthentication,)
	def get(self, request, format=None):
		transaction = Transaction.objects.all()
		serializer = TransactionListSerializer(transaction, many=True)
		return Response(serializer.data)


class TripTransactionList(APIView):
	# authentication_classes = (JSONWebTokenAuthentication,)
	def get(self, request, trip_id, format=None):
		transaction = Transaction.objects.filter(trip=trip_id)
		serializer = TransactionListSerializer(transaction, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = TripTransactionList(data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=HTTP_201_CREATED)
		return Response(serializer.errors, status=HTTP_404_BAD_REQUEST)

class TripUserTransactionList(APIView):
	# authentication_classes = (JSONWebTokenAuthentication,)
	def get(self, request, trip_id, user_id, format=None):
		transaction = Transaction.objects.filter(trip=trip_id,member=user_id)
		serializer = TransactionListSerializer(transaction, many=True)
		return Response(serializer.data)


class TransactionDetails(APIView):
	# authentication_classes = (JSONWebTokenAuthentication,)
	def get(self, request, pk, format=None):
		transaction = Transaction.objects.get(pk=pk)
		serializer = TransactionListSerializer(transaction)
		return Response(serializer.data)

	def delete(self, request, pk, format=None):
		transaction = Transaction.get(pk)
		transaction.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
