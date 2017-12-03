from bs4 import BeautifulSoup
from selenium import webdriver
stock_file = r"C:\Users\Tut10\Desktop\PSTool-Python\Final\test.txt"

def Costco_Shipping(url):
    """This opens up chrome. Scans through the webpage for the out of stock class
    prints out if in stock or out and writes it to file. Pretty simple
    """
    
    driver = webdriver.Chrome(r"C:\Users\Tut10\Desktop\PSTool-Python\chromedriver.exe")
    
    driver.get(url)
    
    file_to_write = open(stock_file, "a")
    
    try:
        x = driver.find_element_by_class_name("out-of-stock")
        if x:
            driver.quit()
            file_to_write.write("[-] Out of stock " + url + '\n')
            file_to_write.close()            
            return "\t\t[-] Out of Stock"
    except:
        driver.quit()
        file_to_write.close() 
        return "\t\t[+] In Stock"
    

def Home_Depot_Shipping(url):
    """This opens up chrome. Scans through the webpage for the id buybelt
    and then creates a list of all the items in buybelt with the class u__text--sucess. 
    Then it chooses the second one in the list, the correct one shipping, not pickup or delivery
    and saves it in a variable called shipping
    """
    
    driver = webdriver.Chrome(r"C:\Users\Tut10\Desktop\PSTool-Python\chromedriver.exe")
    driver.get(url)
    
    # open a file to write to
    file_to_write = open(stock_file, "a")
    
    # send that file to me via email or text
    
    free_delivery = driver.find_elements_by_xpath(r'//*[@id="buybelt"]/div[2]/div[2]/div/div[2]')
    
    # Now it checks both for it
    try:
        if "Free Delivery" in free_delivery[0].text:
            driver.quit()
            file_to_write.close()
            return "\t\t[+] Free Delivery"
        elif "Get it as soon as tomorrow" or "Schedule delivery to your home or jobsite" in free_delivery[0].text:
            driver.quit()
            #file_to_write.write("Cell: " + str(cell) + "[*] Express Delivery " + url + '\n')
            file_to_write.write("[*] Express Delivery " + url + "\n")
            file_to_write.close()
            return "\t\t[*] Express Delivery"
        else:    
            driver.quit()
            file_to_write.write("[-] Out of stock %s\n" % url)
            file_to_write.close()
            return "\t\t[-] Out of stock!"
    except Exception as e:
        driver.quit()
        print(e)    

def Kohls_Shipping(url):
    pass

def BedBathBeyond_Shipping(url):
    pass