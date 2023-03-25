# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 17:00:42 2023

@author: Mahmoud Saeed
"""

from Queries import create_list , insert_list
import mysql.connector as connector

def connect():
    conn = connector.connect(user = 'root' , password = "#######",
                             auth_plugin = 'mysql_native_password')
    cursor = conn.cursor()
    return cursor , conn

def createDB(cur , conn):
    cur.execute("create database supermarketSales")
    cur.execute("use supermarketSales")
    conn.commit()
    return

def createTables(cur , conn):
    for i in create_list:
        cur.execute(i)
        conn.commit()
    return

def insertTables(cur , conn):
    for i in insert_list:
        cur.execute(i)
        conn.commit()
    return


cur , conn = connect()
createDB(cur, conn)
createTables(cur, conn)
insertTables(cur, conn)

