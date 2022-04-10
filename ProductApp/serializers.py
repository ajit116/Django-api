from statistics import mode
from rest_framework import serializers
from ProductApp.models import ProductMaster, BranchMaster, PurchaseOrders, Sales


class BranchMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchMaster
        fields = ('BranchID','BranchName','City')


class ProductMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMaster
        fields = ('ProductID','ProductName','Category')
        


class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = ('Date','ProductID','BranchID','Price','Quantity')


class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrders
        fields = ('Date','PurchaseOrderId','ProductId','BranchId','SupplierId','OrderedQuantity','ReceivedQuantity','OrderedDate','ReceivedDate')
