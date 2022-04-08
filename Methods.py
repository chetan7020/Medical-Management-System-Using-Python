# -*- coding: utf-8 -*-
"""
    @author: Tom Marvolo Riddle
"""

import mysql.connector
import Drugs
import Sales
import Company
import Warnings

class Database :
    
    def connectToDatabase():
        
        database = mysql.connector.connect(
                
                    host = 'localhost' ,
                    username = 'root' ,
                    password = '' ,
                    database = 'medical_management'
                )
        return database   
    
    
class Common :
    
    def exit(self):
        
        logout = input("\n\n   Really want to LOGOUT ? [y / n] : ")
        
        if(logout == "y") :
            
            print("\n\n   Thank you  | See you again !!!")
            print("\n   Build | ..... | Peace \n\n\t\t msg from TMR")
            
        else :
            
            Common.main_menu(self)
        
    def enter_choice(self):
        choice = int(input("\n\n   Enter your choice : "))
        return choice
    
    def main_menu(self):
        
        database = Database.connectToDatabase()
        
        cursor = database.cursor()
        
        sql = "DELETE FROM `mm_warning`"
        
        cursor.execute(sql)
        
        database.commit()
        
        sql = "SELECT * FROM `mm_drugs` WHERE `Quantity` < 10"
        
        cursor.execute(sql)
        
        result = cursor.fetchall()
        
        for i in result :
            
                sql = "INSERT INTO `mm_warning`(`Name`, `Type`, `Quantity`) VALUES (%s,%s,%s)"
                
                values = ( i[1] , i[2] , i[7])
                
                cursor.execute(sql , values)
                
                database.commit()
                
        print("\n\n   1  ---------  Drugs\n   2  ---------  Sales\n   3  ---------  Company\n   4  ---------  Warning\n   5  ---------  Logout")
        
        choice = Common.enter_choice(self)
        
        Common.check_condition(self , choice)
        
        
    def check_condition(self , choice): 
        inner_choice = 0
        
        if(choice == 1): #Drugs
            Drugs.Drugs.add_delete_update(self)
            inner_choice = Common.enter_choice(self)
            #Menu.inner_check_condition(self , inner_choice)
            Drugs.Drugs.inner_check_condition(self , inner_choice)
        
        elif(choice == 2): #sales
            Sales.Sales.view_total(self)
            inner_choice = Common.enter_choice(self)
            Sales.Sales.inner_check_condition(self , inner_choice)
        
        elif(choice == 3): #company
            Company.Company.view(self)
            inner_choice = Common.enter_choice(self)
            Company.Company.inner_check_condition(self , inner_choice)
        
        elif(choice == 4): #warning
            Warnings.Warnings.view(self)
            inner_choice = Common.enter_choice(self)
            Warnings.Warnings.inner_check_condition(self , inner_choice)
        
        elif(choice == 5): #exit
            Common.exit(self)
        
        else :
            Common.exit(self)
    
    