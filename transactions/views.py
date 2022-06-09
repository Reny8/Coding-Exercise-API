from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Transactions
from .serializers import TransactionsSerializer

@api_view(['GET'])
def transactions_details(request):
    if request.method == 'GET':
        transactions = Transactions.objects.all()
        serializer = TransactionsSerializer(transactions, many = True)
        return Response(serializer.data, status.HTTP_200_OK)
