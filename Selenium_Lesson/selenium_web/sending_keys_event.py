#run from command line 
#pip install webdriver-manager

#Searching through the web page by elements
print("****************************************************")
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys 

#Send keys method
def send_keys_method(element, *key):
    element.send_keys(key) 

def main():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    firstName = driver.find_element(By.NAME, "firstname")
    lastName = driver.find_element(By.NAME, "lastname")
    email = driver.find_element(By.NAME, "email")
    phoneN = driver.find_element(By.NAME, "phone")
    
    send_keys_method(firstName, "Adetomiwa")
    send_keys_method(lastName, "Aderinto")
    send_keys_method(email, "aderintoadetomiwa@gmail.com")
    send_keys_method(phoneN, "08063154443")

    #send_keys_method(phoneN, Keys.CONTROL, "v") if you want to do a paste

    driver.close()

   


if __name__ == '__main__':
    main()