# -*- coding: utf-8 -*-
"""
    @author: Tom Marvolo Riddle
"""
import Methods 
from datetime import date

class Drugs :
        
    def add_delete_update(self):
        print("\n\n   1  ---------  View\n   2  ---------  Add\n   3  ---------  Update\n   4  ---------  Delete\n   5  ---------  Add to Sales\n   6  ---------  Go Back")        
     
    def enter_choice(self):
        choice = int(input("\n\n   Enter your choice : "))
        return choice
    
    def inner_check_condition(self , choice):
        
        if(choice == 1): #View
        
            database = Methods.Database.connectToDatabase()
            cursor = database.cursor()
            sql = "select * from mm_drugs"
            cursor.execute(sql)
            result = cursor.fetchall()
            print("\n\n   SN | Name   | Type    | Price | Expiry Day's  | Company | Shelf No. | Quantity |" )
            print(" ------------------------------------------------------------------------------------")
            for i in result:
                print("   ",i[0],"|" , i[1] ,"  |" , i[2] ,"|" , i[3] ,"  |",i[4] ,"           |" , i[5] , " |" , i[6] , "        |" , i[7] , "      |")        
            
            Drugs.add_delete_update(self)
            inner_choice = Drugs.enter_choice(self)
            Drugs.inner_check_condition(self , inner_choice)
        
        elif(choice == 2): #Add
        
            database = Methods.Database.connectToDatabase()
            cursor = database.cursor()
            sql = "select * from mm_drugs"
            cursor.execute(sql)
            result = cursor.fetchall()
            print("\n\n   SN | Name   | Type    | Price | Expiry Day's  | Company | Shelf No. | Quantity |" )
            print(" ------------------------------------------------------------------------------------")
            for i in result:
                print("   ",i[0],"|" , i[1] ,"  |" , i[2] ,"|" , i[3] ,"  |",i[4] ,"           |" , i[5] , " |" , i[6] , "        |" , i[7] , "      |")        
            
            dName = input("\n   Enter Name of Drugs : ")
            dType = input("\n   Enter Type of Drugs : ")
            dPrice = input("\n   Enter Price of Drugs : ")
            dExpiryDay = input("\n   Enter Expiry Days of Drugs : ")
            dCompany = input("\n   Enter Company of Drugs : ")
            dCompanyAdd = input("\n   Enter Company Address : ")
            dCompanyPhoneNumber = input("\n   Enter Company Phone Number : ")
            dShelfNo = input("\n   Enter Shelf Number of Drugs : ")
            dQuantity = input("\n   Enter Quantity of Drugs : ")
            
            sql = "INSERT INTO `mm_drugs`(`Name`, `Type`, `Price`, `Expiry day's`, `Company`, `Shelf No.`, `Quantity`) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            
            values = (dName , dType , dPrice , dExpiryDay ,dCompany ,  dShelfNo , dQuantity)  
            
            cursor.execute(sql , values)
            
            rowcount = cursor.rowcount
            
            database.commit()
            
            sql = "SELECT `Name` FROM `mm_company` WHERE `Name` = %s"
            
            cursor.execute(sql , (dCompany , ))
            
            result = cursor.fetchall()
            
            if(cursor.rowcount == 0) :
                
                sql = "INSERT INTO `mm_company`(`Name`, `Address`, `Phone No.`) VALUES (%s,%s,%s)"
                
                values = (dCompany , dCompanyAdd , dCompanyPhoneNumber)
                
                cursor.execute(sql , values)
                
                database.commit()        
            
            print("\n  " , rowcount , "Row inserted.")
            
            yn = input("\n   Want to add more records ?[y / n] : ")
            
            if(yn == "y") :
                Drugs.inner_check_condition(self , 1)
            else :
                Drugs.add_delete_update(self)
                inner_choice = Drugs.enter_choice(self)
                Drugs.inner_check_condition(self , inner_choice)
            
        elif(choice == 3): #Update
            database = Methods.Database.connectToDatabase()
            cursor = database.cursor()
            sql = "select * from mm_drugs"
            cursor.execute(sql)
            result = cursor.fetchall()
            print("\n\n   SN | Name   | Type    | Price | Expiry Day's  | Company | Shelf No. | Quantity |" )
            print(" ------------------------------------------------------------------------------------")
            for i in result:
                print("   ",i[0],"|" , i[1] ,"  |" , i[2] ,"|" , i[3] ,"  |",i[4] ,"           |" , i[5] , " |" , i[6] , "        |" , i[7] , "      |")        
            
            updateRow = input("\n   Which row you want to select? : ")
            
            sql = "SELECT * FROM mm_drugs WHERE SN = %s"
            
            cursor.execute(sql , (updateRow , ))
            
            result = cursor.fetchall()
            
            for i in result :
                print("\n   1.Name :" , i[1])
                print("\n   2.Type :" , i[2])
                print("\n   3.Price :" , i[3])
                print("\n   4.Expiry Day's :" , i[4])
                print("\n   5.Company :" , i[5])
                print("\n   6.Shelf Number :" , i[6])
                print("\n   7.Quantity :" , i[7])
            
            updateField = input("\n   Which field you want to update? : ")
            
            if(updateField == '1') :
                
                sql = "UPDATE `mm_drugs` SET `Name`= %s WHERE SN = %s"
                
                dName = input("\n   Enter Name of Drugs : ")
                
                cursor.execute(sql , (dName , updateRow , ))
                
                database.commit()
                
                print("Drugs Name Updated Successfully !!!")
                
                yn = input("\n   Want to update more records ?[y / n] : ")
            
                if(yn == "y") :
                    Drugs.inner_check_condition(self , 3)
                else :
                    Drugs.add_delete_update(self)
                    inner_choice = Drugs.enter_choice(self)
                    Drugs.inner_check_condition(self , inner_choice)
                    
            elif(updateField == '2') :
                
                sql = "UPDATE `mm_drugs` SET `Type`= %s WHERE SN = %s"
                
                dType = input("\n   Enter Type of Drugs : ")
                
                cursor.execute(sql , (dType , updateRow , ))
                
                database.commit()
                
                print("\n   Drugs Type Updated Successfully !!!")
                
                yn = input("\n   Want to update more records ?[y / n] : ")
            
                if(yn == "y") :
                    Drugs.inner_check_condition(self , 3)
                else :
                    Drugs.add_delete_update(self)
                    inner_choice = Drugs.enter_choice(self)
                    Drugs.inner_check_condition(self , inner_choice)
                    
            elif(updateField == '3') :
                
                sql = "UPDATE `mm_drugs` SET `Price`= %s WHERE SN = %s"
                
                dPrice = input("\n   Enter Price of Drugs : ")
                
                cursor.execute(sql , (dPrice , updateRow , ))
                
                database.commit()
                
                print("\n   Drugs Price Updated Successfully !!!")
                
                yn = input("\n   Want to update more records ?[y / n] : ")
            
                if(yn == "y") :
                    Drugs.inner_check_condition(self , 3)
                else :
                    Drugs.add_delete_update(self)
                    inner_choice = Drugs.enter_choice(self)
                    Drugs.inner_check_condition(self , inner_choice)
                
            elif(updateField == '4') :
                sql = "UPDATE `mm_drugs` SET `Expiry day's`= %s WHERE SN = %s"
                
                dExpiryDay = input("\n   Enter Expiry Days of Drugs : ")
                
                cursor.execute(sql , (dExpiryDay , updateRow , ))
                
                database.commit()
                
                print("\n   Drugs Expiry Day's Updated Successfully !!!")
                
                yn = input("\n   Want to update more records ?[y / n] : ")
            
                if(yn == "y") :
                    Drugs.inner_check_condition(self , 3)
                else :
                    Drugs.add_delete_update(self)
                    inner_choice = Drugs.enter_choice(self)
                    Drugs.inner_check_condition(self , inner_choice)
                
            elif(updateField == '5') :
                sql = "UPDATE `mm_drugs` SET `Company`= %s WHERE SN = %s"
                
                dCompany = input("\n   Enter Company of Drugs : ")
                
                cursor.execute(sql , (dCompany , updateRow , ))
                
                database.commit()
                
                print("\n   Drugs Company Updated Successfully !!!")
                
                yn = input("\n   Want to update more records ?[y / n] : ")
            
                if(yn == "y") :
                    Drugs.inner_check_condition(self , 3)
                else :
                    Drugs.add_delete_update(self)
                    inner_choice = Drugs.enter_choice(self)
                    Drugs.inner_check_condition(self , inner_choice)
            
            elif(updateField == '6') :
                sql = "UPDATE `mm_drugs` SET `Shelf No.`= %s WHERE SN = %s"
                
                dShelfNo = input("\n   Enter Shelf Number of Drugs : ")
                
                cursor.execute(sql , (dShelfNo , updateRow , ))
                
                database.commit()
                
                print("\n   Drugs Shelf Number Updated Successfully !!!")
                
                yn = input("\n   Want to update more records ?[y / n] : ")
            
                if(yn == "y") :
                    Drugs.inner_check_condition(self , 3)
                else :
                    Drugs.add_delete_update(self)
                    inner_choice = Drugs.enter_choice(self)
                    Drugs.inner_check_condition(self , inner_choice)
                
            elif(updateField == '7') :
                sql = "UPDATE `mm_drugs` SET `Quantity` = %s WHERE SN = %s"
                
                dQuantity = input("\n   Enter Quantity of Drugs : ")
                
                cursor.execute(sql , (dQuantity , updateRow , ))
                
                database.commit()
                
                print("\n   Drugs Quantity Updated Successfully !!!")
                
                yn = input("\n   Want to update more records ?[y / n] : ")
            
                if(yn == "y") :
                    Drugs.inner_check_condition(self , 3)
                else :
                    Drugs.add_delete_update(self)
                    inner_choice = Drugs.enter_choice(self)
                    Drugs.inner_check_condition(self , inner_choice)
            
        elif(choice == 4): #Delete
            database = Methods.Database.connectToDatabase()
            cursor = database.cursor()
            sql = "select * from mm_drugs"
            cursor.execute(sql)
            result = cursor.fetchall()
            print("\n\n   SN | Name   | Type    | Price | Expiry Day's  | Company | Shelf No. | Quantity |" )
            print(" ------------------------------------------------------------------------------------")
            for i in result:
                print("   ",i[0],"|" , i[1] ,"  |" , i[2] ,"|" , i[3] ,"  |",i[4] ,"           |" , i[5] , " |" , i[6] , "        |" , i[7] , "      |")        
            
            deleteRow = input("\n   Which row you want to delete? : ")
            
            sql = "DELETE FROM `mm_drugs` WHERE SN = %s"
            
            cursor.execute(sql , (deleteRow, ))
            
            database.commit()
            
            print("\n  " , cursor.rowcount , "Row Deleted.")
            
            yn = input("\n   Want to delete more records ?[y / n] : ")
            
            if(yn == "y") :
                Drugs.inner_check_condition(self , 4)
            else :
                Drugs.add_delete_update(self)
                inner_choice = Drugs.enter_choice(self)
                Drugs.inner_check_condition(self , inner_choice)         

        elif(choice == 5): #Add to Sale
            database = Methods.Database.connectToDatabase()
            cursor = database.cursor()
            sql = "select * from mm_drugs"
            cursor.execute(sql)
            result = cursor.fetchall()
            print("\n\n   SN | Name   | Type    | Price | Expiry Day's  | Company | Shelf No. | Quantity |" )
            print(" ------------------------------------------------------------------------------------")
            for i in result:
                print("   ",i[0],"|" , i[1] ,"  |" , i[2] ,"|" , i[3] ,"  |",i[4] ,"           |" , i[5] , " |" , i[6] , "        |" , i[7] , "      |")        
            
            addToSalesRow = input("\n   Which row you want to add to sales? : ")

            sql = "SELECT * FROM `mm_drugs` WHERE SN = %s"
            
            cursor.execute(sql , (addToSalesRow , ))
            
            result = cursor.fetchall()
            
            deductQuantity = int(input("\n   How much drugs you want to sale? : "))
            
            if(deductQuantity <= int(result[0][7])) :
                
                todayDate = date.today()
                
                recalculatedQuantity = int(result[0][7]) - deductQuantity
                
                if(recalculatedQuantity < 0) :             
                    print("\n\n   Cann't add more drugs than available.")
                    
                else :
                    totalPrice = recalculatedQuantity * int(result[0][3])
                    
                    sql = "UPDATE `mm_drugs` SET `Quantity` = %s WHERE SN = %s"
                    
                    cursor.execute(sql , (str(recalculatedQuantity) , addToSalesRow , ))    
                                  
                    sql = "INSERT INTO `mm_sales`(`Name`, `Type`, `Price`, `Quantity`, `Total Price`, `Date`) VALUES (%s,%s,%s,%s,%s,%s)"
                    
                    cursor.execute(sql , ( str(result[0][1]) , str(result[0][2]) , str(result[0][3]) , str(recalculatedQuantity) , str(totalPrice) , str(todayDate) , ))
                    
                    print("\n  ",cursor.rowcount,"Row of Drugs Added to Sales Successfully." )
                    
                    sql = "DELETE FROM `mm_drugs` WHERE `Quantity` = 0"
                    
                    cursor.execute(sql)
                    
                    database.commit()  
                    
                    yn = input("\n   Want to add more records to sales?[y / n] : ")
                
                    if(yn == "y") :
                        Drugs.inner_check_condition(self , 5)
                    else :
                        Drugs.add_delete_update(self)
                        inner_choice = Drugs.enter_choice(self)
                        Drugs.inner_check_condition(self , inner_choice)
                         
            
        elif(choice == 6): #Go Back
            Methods.Common.main_menu(self)
            
        else :
            Methods.Common.exit(self)