from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Transactions
from .serializers import TransactionsSerializer

@api_view(['GET', 'POST'])
def transactions_details(request):
    if request.method == 'GET':
        transactions = Transactions.objects.all()
        serializer = TransactionsSerializer(transactions, many = True)
        return Response(serializer.data, status.HTTP_200_OK)
    if request.method == 'POST': 
        serializer = TransactionsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


