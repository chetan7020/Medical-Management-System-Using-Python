# -*- coding: utf-8 -*-
"""
    @author: Tom Marvolo Riddle
"""
import time
import Methods

class Menus:
    
    def __init__(self):
        Menus.heading(self)
    
    def enter_user_pass(self):
        username = input("Enter Username : ")
        password = input("Enter Password : ")    
        print(username + " " +password)     
        
    def check_user_pass(self , username , password):
        print("Username : " + username + "\nPassword : " + password)
        
    def heading(self):
        print("  ---------------------------------------------------")
        print("  ---------------------------------------------------")
        print("  -----------  MEDICAL MANAGEMENT SYSTEM  -----------")
        print("  ---------------------------------------------------")
        print("  ---------------------------------------------------")
        #time.sleep(4)
        Methods.Common.main_menu(self)

            
obj = Menus() 
