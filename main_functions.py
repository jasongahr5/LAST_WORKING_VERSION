# WRITTEN BY JASON GAHR 2017


import os, webbrowser, sys, requests, openpyxl
from selenium import webdriver
from bs4 import BeautifulSoup
from time import gmtime, strftime
import shipping_functions


# Quickly divide our file up so we know which section is which
notworkfile = open(r"C:\Users\Tut10\Desktop\PSTool-Python\nsf.txt", "a")

notworkfile.write("=============================================================")
notworkfile.write(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
notworkfile.write("=============================================================\n")
notworkfile.close()

def change_directory():
    """This function changes directories to the business folder"""
    print("[*] Current directory is %s.\n[*] Changing Directories Now!" % os.getcwd())
    wanted_directory = r"C:\Users\Tut10\OneDrive\Business"
    try:
        # Attempts to change directories to where the excel file containing all the links are
        os.chdir(wanted_directory)
        #os.chdir(r"C:\Users\Tut10\OneDrive\Business")
        print("[+] Successfully Changed Directories!")
        print("[*] Current directory is %s." % os.getcwd())
    except:
        # TODO Fix this so it prints an error to a file of what went wrong
        print("[-]Something went wrong")  
    return

def download_links():
    """This function opens the file the excel file. Then it downloads the webpage, then it searches for my global
    variable of free shipping that i have listed at the beginning in the content of the web page. Then it prints to the
    excel file that in that row of the item saying what type of shipping it is"""
    
    print("[*] Opening file")
    exfile = "Products - GorillaDealsToday.xlsx"
    #wb = openpyxl.load_workbook('Products - GorillaDealsToday.xlsx')
    wb = openpyxl.load_workbook(exfile)
    #The tab we want is called Cost
    extab = "Active Items"
    #sheet = wb.get_sheet_by_name('Cost')
    sheet = wb.get_sheet_by_name(extab)
    #This loops through each row in the B column, then it prints it out. The variable cell is what you want. contains the link
    #exrows = input("Put in the rows you want to iterate through. Example: 'B4:B37': ")
    for row in sheet.iter_rows("B4:B37"):
        for cell in row:
            if "homedepot.com" in cell.value:
                stock = shipping_functions.Home_Depot_Shipping(cell.value)
            
            elif "costco.com" in cell.value:
                stock = shipping_functions.Costco_Shipping(cell.value)
            else:
                print("[!] Not Home Depot or Costco Item")
            print("\t[+] Item: %s" % cell.value)
            print(stock)
            
                
    print("[*] Finished lopping thru!")
    
    print("[*] Closing excel file")
    wb.close()
    return 


    
    
