from rest_framework import serializers
from .models import Transactions

class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = ['id','payer','points','timestamp']