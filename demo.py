import os
from selenium import webdriver
import re
from googlesearch import search

def zipcode_match(pin, add):      #extract pin from address and matches with input fun1
    in_zip = r'(\d{6})'
    pin_code = re.search(in_zip, add)
    if(pin==pin_code):
        return True
    return False 

def ifindiamart(aaa):           #checks if the first link is indiamart fun2
    ind = r'^.*(\bindiamart\b)?.*$'
    ind_search = re.search(ind, aaa)
    if(ind_search == 'indiamart'):
        return True
    return False


path = '/TataAig'

# from selenium.webdriver.firefox.options import Options
# opts = Options()
# opts.set_headless()
# assert opts.headless  # Operating in headless mode
# browser = Firefox(options=opts)
# browser.get('https://duckduckgo.com')

input1 = "name"
input2 = "pin"

# to search
query = "Geeksforgeeks"
 
for j in search(query, tld="co.in", num=1, stop=1, pause=2):   
    h = j   #https://www.geeksforgeeks.org/performing-google-search-using-python-code/
    print(j)





from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(h)
