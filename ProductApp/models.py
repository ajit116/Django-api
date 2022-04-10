#from tkinter.messagebox import YES
#from tkinter.tix import Tree
from django.db import models

#from ProductApp.apps import ProductappConfig

# Create your models here.
class ProductMaster(models.Model):
    ProductID = models.IntegerField(primary_key=True)
    ProductName = models.CharField(max_length=200)
    Category = models.CharField(max_length=200)


class BranchMaster(models.Model):
    BranchID = models.IntegerField(primary_key=True)
    BranchName = models.CharField(max_length=200)
    City = models.CharField(max_length=200)


class PurchaseOrders(models.Model):
    Date = models.DateField()
    PurchaseOrderId = models.IntegerField(primary_key=True)
    ProductId = models.ForeignKey(ProductMaster, on_delete= models.CASCADE, null = False)
    BranchId = models.ForeignKey(BranchMaster, on_delete= models.CASCADE, null = False)
    SupplierId = models.IntegerField()
    OrderedQuantity = models.IntegerField()
    ReceivedQuantity = models.IntegerField(blank=True, null=True)
    OrderedDate = models.DateField()
    ReceivedDate = models.DateField(blank=True, null=True)


class Sales(models.Model):
    Date = models.DateField()
    ProductID = models.ForeignKey(ProductMaster, on_delete= models.CASCADE, null = False)
    BranchID = models.ForeignKey(BranchMaster, on_delete= models.CASCADE, null = False)
    Price = models.IntegerField()
    Quantity = models.IntegerField()

