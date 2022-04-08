# -*- coding: utf-8 -*-
"""
    @author: Tom Marvolo Riddle
"""
import Methods

class Warnings :
    
    def view(self):
        print("\n\n   1  ---------  View\n   2  ---------  Go Back")        
     
    def enter_choice(self):
        choice = int(input("\n\n   Enter your choice : "))
        return choice
    
    def inner_check_condition(self , choice):
        
        if(choice == 1): #View
        
            database = Methods.Database.connectToDatabase()
            cursor = database.cursor()
            sql = "select * from mm_warning"
            cursor.execute(sql)
            result = cursor.fetchall()
            print("\n\n   Company Name   | Drugs Type    | Remaining Quantity |" )
            print(" ----------------------------------------------------------") 
            for i in result:
                print("  ",i[0],"          |" , i[1] ,"     |" , i[3], "                 |")        
            
            Warnings.view(self)
            inner_choice = Warnings.enter_choice(self)
            Warnings.inner_check_condition(self , inner_choice)
            
        elif(choice == 2): #Go Back
            Methods.Common.main_menu(self)
            
        else :
            Methods.Common.exit(self)
