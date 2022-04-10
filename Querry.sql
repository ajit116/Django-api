-- branchmaster
insert into ProductApp_branchmaster
(BranchID,BranchName,City)
values
(100,'Powai','Mumbai'),
(200,'HSR','Bangalore')
;
select * from ProductApp_branchmaster;

-- productmaster
insert or ignore into ProductApp_productmaster
(ProductID,ProductName,Category)
values
(1,'Tropicana Orange Juice','Drinks'),
(2,'Bourbon','Biscuits'),
(2,'Bourbon','Biscuits')
;
select * from ProductApp_productmaster;

-- sales
insert or ignore into ProductApp_sales
(Date,ProductID_id,BranchID_id,Price,Quantity)
values
('2021-11-01',1,100,10,120),
('2021-11-01',2,200,15,450),
('2021-11-02',1,100,12,300),
('2021-11-02',2,200,20,500)
; 

-- purchaseorders
insert into ProductApp_purchaseorders
(Date, PurchaseOrderId,ProductID_id, BranchId_id, SupplierId, OrderedQuantity,ReceivedQuantity, OrderedDate,ReceivedDate)
values
('2021-11-01',101,1,100,2000,100,null ,'2021-11-01',null ),
('2021-11-01',102,1,100,2000,50,50,'2021-10-25','2021-11-01'),
('2021-11-01',103,1,100,2000,20,20,'2021-10-28','2021-11-01'),
('2021-11-01',104,2,200,3000,200,200,'2021-11-01','2021-11-01'),
('2021-11-01',105,2,200,3000,50,50,'2021-10-27','2021-11-01'),
('2021-11-01',106,2,200,3000,20,20,'2021-10-29','2021-11-01')
;
select * from ProductApp_purchaseorders;
