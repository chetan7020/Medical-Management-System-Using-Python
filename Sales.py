# -*- coding: utf-8 -*-
"""
@author: Tom Marvolo Riddle
"""

import Methods
from datetime import date

class Sales :
    
    def view_total(self):
        print("\n\n   1  ---------  View\n   2  ---------  Today Total\n   3  ---------  Grand Total\n   4  ---------  Go Back")        
     
    def enter_choice(self):
        choice = int(input("\n\n   Enter your choice : "))
        return choice
    
    def inner_check_condition(self , choice):
        
        if(choice == 1): #View
        
            database = Methods.Database.connectToDatabase()
            cursor = database.cursor()
            sql = "select * from mm_sales"
            cursor.execute(sql)
            result = cursor.fetchall()
            print("\n\n   SN | Name   | Type    | Price | Quantity | Total Price | Date" )
            print(" ------------------------------------------------------------------------------------")
            for i in result:
                print("   ",i[0],"|" , i[1] ,"  |" , i[2] ,"|" , i[3] ,"  |",i[4] ," | ",i[5] , "      |",i[6] , "      |")        
            
            Sales.view_total(self)
            inner_choice = Sales.enter_choice(self)
            Sales.inner_check_condition(self , inner_choice)
            
        elif(choice == 2) :
            
            todayTotal = 0
            todayDate = date.today()
            database = Methods.Database.connectToDatabase()
            cursor = database.cursor()
            sql = "SELECT `Total Price` FROM `mm_sales` WHERE `Date` = %s"
            cursor.execute(sql , (str(todayDate) , ))
            result = cursor.fetchall()
            for i in result :
                todayTotal += int(i[0])
            print("\n\n   Today Total =",todayTotal,"₹")
            Sales.view_total(self)
            inner_choice = Sales.enter_choice(self)
            Sales.inner_check_condition(self , inner_choice)
            
        elif(choice == 3) :
            
            grandTotal = 0
            todayDate = date.today()
            database = Methods.Database.connectToDatabase()
            cursor = database.cursor()
            sql = "SELECT `Total Price` FROM `mm_sales`"
            cursor.execute(sql)
            result = cursor.fetchall()
            for i in result :
                grandTotal += int(i[0])
            print("\n\n   Grand Total =",grandTotal,"₹")
            Sales.view_total(self)
            inner_choice = Sales.enter_choice(self)
            Sales.inner_check_condition(self , inner_choice)
        
        elif(choice == 4): #Go Back
            Methods.Common.main_menu(self)
            
        else :
            Methods.Common.exit(self)