from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Transactions
from .serializers import TransactionsSerializer

@api_view(['GET', 'POST'])
def transactions_details(request):
    # GETTING ALL THE TRANSACTIONS IN THE DATABASE
    if request.method == 'GET':
        transactions = Transactions.objects.all().order_by("timestamp")
        serializer = TransactionsSerializer(transactions, many = True)
        return Response(serializer.data, status.HTTP_200_OK)

    # ADDING A NEW TRANSACTION
    elif request.method == 'POST': 
        serializer = TransactionsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST) 

@api_view(['PUT'])
def spend_points(request,points):
    #SPENDING POINTS
    if request.method == 'PUT':
        # ORDERED THE TRANSACTIONS FROM OLDEST POINTS
        transactions = Transactions.objects.all().order_by("timestamp")
        for trans in transactions: 
            trans.points -= points
            # WHEN POINTS FOR TO NEGATIVE DISPLAY WILL BE 0
            if trans.points < 0:
                points = abs(trans.points)
                trans.points = 0
                serializer = TransactionsSerializer(trans, data = request.data, partial = True)
                if serializer.is_valid(raise_exception = True):
                    serializer.save()
            elif trans.points >= 0:
                points = 0
                serializer = TransactionsSerializer(trans, data = request.data, partial = True)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
            serializer_all = TransactionsSerializer(transactions, many=True)
            return Response(serializer_all.data, status.HTTP_202_ACCEPTED)
            
           
                

                


    

