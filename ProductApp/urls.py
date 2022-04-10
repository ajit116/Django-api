from django.urls import re_path as url
from ProductApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    #question 1
    url(r'JoinOperationAPI$', views.JoinOperationAPI),

    #question 2 (a)
    url(r'LeadTimeAPI$', views.LeadTimeOperationAPI),

    #question 2 (b) 
    url(r'AvgAPI$', views.AvgAPI),

    #Question 3
    url(r'sales$', views.SalesAPI),
    url(r'sales/([0-9]+)$',views.SalesAPI),
    
    url(r'purchase$', views.PurchaseOrderAPI),
    url(r'purchase/([0-9]+)$',views.PurchaseOrderAPI),


    
    
]