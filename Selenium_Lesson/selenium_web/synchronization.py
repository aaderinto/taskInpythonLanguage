#run from command line 
#pip install webdriver-manager

#Searching through the web page by elements
print("****************************************************")
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys 
from selenium.webdriver.support.ui import WebDriverWait #the import line that allows the wait of 20secs
from selenium.webdriver.support import expected_conditions as EC

#Send keys method
def clickable_method(element):
    web_driver_wait = WebDriverWait(element, 20) #waits 20sec for the element
    web_driver_wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Academy'))) #checks if the element is clickable for 20secs
    academy_link = element.find_element(By.LINK_TEXT, 'Academy')
    academy_link.click()
    time.sleep(10)

def main():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")

    clickable_method(driver)

    driver.close()

   


if __name__ == '__main__':
    main()