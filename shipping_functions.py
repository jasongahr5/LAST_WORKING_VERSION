from bs4 import BeautifulSoup
from selenium import webdriver
file_to_write = r"C:\Users\Tut10\Desktop\PSTool-Python\Final\test.txt"

def Costco_Shipping(url):
    """This opens up chrome. Scans through the webpage for the out of stock class
    prints out if in stock or out and writes it to file. Pretty simple
    """
    
    driver = webdriver.Chrome(r"C:\Users\Tut10\Desktop\PSTool-Python\chromedriver.exe")
    
    driver.get(url)
    
    notworkfile = open(file_to_write, "a")
    
    try:
        x = driver.find_element_by_class_name("out-of-stock")
        if x:
            driver.quit()
            notworkfile.write("[-] " + url + '\n')
            notworkfile.close()            
            return "\t\t[-] Out of Stock"
    except:
        driver.quit()
        notworkfile.close() 
        return "\t\t[+] In Stock"
    

def Home_Depot_Shipping(url):
    """This opens up chrome. Scans through the webpage for the id buybelt
    and then creates a list of all the items in buybelt with the class u__text--sucess. 
    Then it chooses the second one in the list, the correct one shipping, not pickup or delivery
    and saves it in a variable called shipping
    """
    
    driver = webdriver.Chrome(r"C:\Users\Tut10\Desktop\PSTool-Python\chromedriver.exe")
    driver.get(url)
    soup = BeautifulSoup(driver.page_source,"lxml")
    driver.quit()
    
    # open a file to write to
    notworkfile = open(file_to_write, "a")
    
    # send that file to me via email or text
     
    for title in soup.select("#buybelt"):
        try:
            shipping = title.select(".u__text--success")[1].text.strip()
        except:
            shipping = title.select(".u__text--success")
        
        finally:
            if shipping == "Free Delivery": 
                notworkfile.close()   
                return "\t\t[+] Free Delivery"         
            else: # write to file which ones don't work
                notworkfile.write("[-] " + url + '\n')
                notworkfile.close()
                return "\t\t[-] Not Free Delivery or Out of Stock"

def Kohls_Shipping(url):
    pass

def BedBathBeyond_Shipping(url):
    pass