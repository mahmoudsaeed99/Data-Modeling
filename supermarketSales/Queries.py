# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 16:07:01 2023

@author: Mahmoud Saeed
"""

# create_table_Employees = """
#     create table Employees(employeeID int auto_increment unique ,employeeName varchar(50),
#                            title varchar(25),salary float , primary key(employeeID))

# """


create_table_Products = """
    create table Products(productID int auto_increment unique ,productName varchar(25),
                           productCategory varchar(25),price float , primary key(productID))
"""

create_table_Customers = """
    create table Customers(customerID int auto_increment unique ,customerName varchar(25),
                           city varchar(25) , gender varchar(10),primary key(customerID))
"""

create_table_Locations = """
    create table Locations(locationID int auto_increment unique ,region varchar(25),
                           city varchar(25) , state varchar(10),primary key(locationID))
"""

create_table_Times = """
    create table Time(
    timeID int auto_increment unique, 
    day int, 
    week int, 
    month int,
    quarter int,
    year int,
    primary key(timeID))
"""

create_table_Sales = """
        create table Sales(custID int , locID int,
                           prodID int , timeID int ,
                           quantity int, total_price float,
                           FOREIGN KEY (custID) REFERENCES Customers(customerID),
                           FOREIGN KEY (locID) REFERENCES Locations(locationID),
                           FOREIGN KEY (prodID) REFERENCES Products(productID),
                           FOREIGN KEY (timeID) REFERENCES Time(timeID))
"""



insert_table_products = """
    insert into Products(productName,productCategory,price) values('tiger','snacks',5),
    ('moro','chocolate',8),('domty','cheese',20)
"""

insert_table_customers = """
    insert into Customers(customerName,city,gender) values('mahmoud','Cairo','male'),
    ('marwa','Alex','female')
"""
insert_table_Locations = """
    insert into Locations(region,city,state) values('middleEast','Cairo','helwan')
"""
insert_table_Times = """
    insert into Time(day,week,month,quarter,year) values(4,1,3,1,2020)
"""

insert_table_Sales = """
    insert into Sales(custID,prodID,timeID,locID,quantity,total_price) 
    values(1,1,1,1,3,(select 3*price from Products where productID = 1))
"""


create_list = [create_table_Products,create_table_Customers,create_table_Locations,
               create_table_Times,create_table_Sales]

insert_list = [insert_table_products,insert_table_customers,
               insert_table_Locations,insert_table_Times,insert_table_Sales]

