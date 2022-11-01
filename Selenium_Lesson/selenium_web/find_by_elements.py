#run from command line 
#pip install webdriver-manager

#Searching through the web page by elements

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 



def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/")
    
    #Locating by tag name
    links = driver.find_elements(By.TAG_NAME, 'a')
    for link in links:
           print("Link:", link.text)
    



main()