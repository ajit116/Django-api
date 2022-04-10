from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.db import connection

from ProductApp.models import ProductMaster, BranchMaster, PurchaseOrders, Sales
from ProductApp.serializers import BranchMasterSerializer, ProductMasterSerializer, PurchaseOrderSerializer, SalesSerializer

# Create your views here.
@csrf_exempt
def JoinOperationAPI(request):
    if request.method == 'GET':
        cursor = connection.cursor()
        cursor.execute('''
                        select Date as Sale_Date, ProductID_id as ProductID, BranchID_id as BranchID, Price as Price, Quantity as Quantity, ProductName as ProductName, Category as Category, BranchName as BranchName, City as City
                        from ProductApp_sales s
                        join ProductApp_branchmaster bm on s.BranchID_id = bm.BranchID
                        join ProductApp_productmaster pm on s.ProductID_id = pm.ProductID
                        ;
                        ''')
        solution = cursor.fetchall()
        #purchase_serializer = PurchaseOrderSerializer(purchase , many=True)
        return JsonResponse(solution, safe=False)

@csrf_exempt
def LeadTimeOperationAPI(request):
    if request.method == 'GET':
        cursor = connection.cursor()
        cursor.execute('''select cast ((JulianDay(ReceivedDate) - JulianDay(OrderedDate)) as Integer) as LeadTime,po.*  from ProductApp_purchaseorders po
                        ;
                        ''')
        solution = cursor.fetchall()
        #purchase_serializer = PurchaseOrderSerializer(purchase , many=True)
        return JsonResponse(solution, safe=False)

@csrf_exempt
def AvgAPI(request):
    if request.method == 'GET':
        cursor = connection.cursor()
        cursor.execute('''select  ProductID_id,BranchId_id,SupplierId , avg(cast ((JulianDay(ReceivedDate) - JulianDay(OrderedDate)) as Integer)) as average_time from ProductApp_purchaseorders po
                            group by ProductID_id, BranchId_id, SupplierId;
                        ''')
        solution = cursor.fetchall()
        #purchase_serializer = PurchaseOrderSerializer(purchase , many=True)
        return JsonResponse(solution, safe=False)

# crud operation on PurchaseOrder api call
@csrf_exempt
def PurchaseOrderAPI(request, id=0):
    if request.method == 'GET':
        '''
        cursor = connection.cursor()
        cursor.execute(''''''
                        select Date as Sale_Date, ProductID_id as ProductID, BranchID_id as BranchID, Price as Price, Quantity as Quantity, ProductName as ProductName, Category as Category, BranchName as BranchName, City as City
                        from ProductApp_sales s
                        join ProductApp_branchmaster bm on s.BranchID_id = bm.BranchID
                        join ProductApp_productmaster pm on s.ProductID_id = pm.ProductID
                        ;
                        '''''')
        solution = cursor.fetchall()
        '''
        purchase = PurchaseOrders.objects.all() 
        purchase_serializer = PurchaseOrderSerializer(purchase , many=True)
        return JsonResponse(purchase_serializer.data, safe=False)
    
    elif request.method=='POST':
        purchase_data=JSONParser().parse(request)
        purchase_serializer=PurchaseOrderSerializer(data=purchase_data)
        if purchase_serializer.is_valid():
            purchase_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        purchase_data=JSONParser().parse(request)
        purchase=PurchaseOrders.objects.get(PurchaseOrderId=purchase_data['PurchaseOrderId'])
        purchase_serializer=PurchaseOrderSerializer(purchase,data=purchase_data)
        if purchase_serializer.is_valid():
            purchase_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        purchase=PurchaseOrders.objects.get(PurchaseOrderId=id)
        purchase.delete()
        return JsonResponse("Deleted Successfully",safe=False)

#Sales CRUD [ insert new record in sale ]
@csrf_exempt
def SalesAPI(request, id=0):
    if request.method == 'GET':
        sale = Sales.objects.all() 
        sale_serializer = SalesSerializer(sale , many=True)
        return JsonResponse(sale_serializer.data, safe=False)
    
    elif request.method=='POST':
        sale_data=JSONParser().parse(request)
        sale_serializer=SalesSerializer(data=sale_data)
        if sale_serializer.is_valid():
            sale_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        sale_data=JSONParser().parse(request)
        sale=Sales.objects.get(SaleId=sale_data['id'])
        sale_serializer=SalesSerializer(sale,data=sale_data)
        if sale_serializer.is_valid():
            sale_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        sale=Sales.objects.get(SaleId=id)
        sale.delete()
        return JsonResponse("Deleted Successfully",safe=False)



