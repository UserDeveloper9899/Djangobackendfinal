from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item, Price
from rest_framework.parsers import JSONParser
from.serializers import ItemSerializer
from django.db.models import Q

@api_view(['GET'])
def getData(request):
    if request.method == 'GET':
        items=Item.objects.all()
        serializer=ItemSerializer(items, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def regData(request):
    if request.method == 'POST':
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

@api_view(['DELETE'])
def delData(request, companycode):
    if request.method == 'DELETE':
        items = Item.objects.get(pk=companycode)
        items.delete()
        return Response("Record deleted successfully")

@api_view(['PUT'])
def addData(request, c1):
    try:
        items = Item.objects.get(ccode=c1)
    except Item.DoesNotExist:
        return Response("Item not Found to add stockprice")
    if request.method == 'PUT':
        item_data = JSONParser().parse(request)
        serializer = ItemSerializer(items, data=item_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

@api_view(['GET'])
def fetData(request, c1, sdate, edate):
    if request.method == 'POST':
        #items = Item.objects.get(pk=c1)
        print(sdate)
        items=Item.objects.filter(prices__pk=c1,date__range=[str(sdate),str(edate)])
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def infoData(request, companycode):
    if request.method == 'GET':
        items= Item.objects.filter(pk=companycode)
        serializer=ItemSerializer(items, many=True)
        return Response(serializer.data)