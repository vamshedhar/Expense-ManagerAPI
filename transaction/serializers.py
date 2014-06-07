from rest_framework import serializers
from transaction.models import Transaction

class TransactionListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Transaction
		fields = ('id', 'description', 'amount', 'trip', 'member', 'created_time')

class TripTransactionsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Transaction
		fields = ('id', 'description', 'amount', 'member', 'created_time')

class TransactionDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Transaction
		fields = ('id', 'description', 'amount', 'trip', 'member', 'created_time')