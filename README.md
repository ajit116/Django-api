# Django-api

All the records mentioned in the Sheet have been added in their respective table in SQLite database. using [Querry.sql](https://github.com/ajit116/Django-api/blob/main/Querry.sql)

Futher on going into questions Postman has been used to GET/ POST the records as per the requirements.

1. Create an API to perform operations on Sales, Product Master, and Branch Master to get required results
-> It can be found on http://127.0.0.1:8000/JoinOperationAPI below is the image of Json records fetched from Postman
with **Date, ProductID, BranchID, Price, Quantity, ProductName, Category, BranchName, City** column respectively.
![Postman JoinOperationAPI](https://github.com/ajit116/Django-api/blob/main/images/Join.png)

2. Create an API and use Purchase Orders to calculate the following 2 things:
   a.) Add a column ‘lead time’:  Lead time is the difference between the received date and the ordered date in days<br></br>
    -> This column has been fetched from API(http://127.0.0.1:8000/LeadTimeAPI) and in sql Querry both image of which can be found below
    ![Postman LeadTimeAPI](https://github.com/ajit116/Django-api/blob/main/images/LeadTime.png)
   ![SQL LeadTimeAPI](https://github.com/ajit116/Django-api/blob/main/images/LeadTimeSql.png)
   
   b.)Calculate lead time average for each Product ID-Branch ID-Supplier ID combination.<br>
   -> The below json records are in **ProductID,BranchId,SupplierId,AvgLeadTime** column wise respectively 
    ![Postman AvgLeadTime](https://github.com/ajit116/Django-api/blob/main/images/AvgLeadTime.png)
  
 3. Create an API to insert a new Sales record
    Previous records in Sales Table (http://127.0.0.1:8000/sales)
    ![Postman SaleRecords](https://github.com/ajit116/Django-api/blob/main/images/Prev_salesTable.png)
    <br>New record  **Date Product ID Branch ID Price Quantity**
                _'2021-11-03',  1, 100, 10, 150_ Added using POST method

    ![Postman Added](https://github.com/ajit116/Django-api/blob/main/images/Added_in_sales.png)
    <br> Updated record in Sales API
    ![Postman NewSaleRecords](https://github.com/ajit116/Django-api/blob/main/images/Get_after_adding_record_in_sales.png)
  
