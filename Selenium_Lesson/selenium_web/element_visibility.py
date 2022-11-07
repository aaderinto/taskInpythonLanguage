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

#Send keys method
def send_keys_method(element, *key):
    element.send_keys(key) 

def main():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")

    #To maximize the page
    driver.maximize_window()
    
    send_keys_method(driver.find_element(By.NAME, "firstname"), "Adetomiwa")
    send_keys_method(driver.find_element(By.NAME, "lastname"), "Aderinto")
    send_keys_method(driver.find_element(By.NAME, "email"), "aderintoadetomiwa@gmail.com")
    send_keys_method(driver.find_element(By.NAME, "phone"), "08063154443")

    #send_keys_method(phoneN, Keys.CONTROL, "v") if you want to do a paste
    

    form = driver.find_element(By.TAG_NAME, 'form')
    submit_button = form.find_element(By.TAG_NAME, 'button')
    
    #To check for visibility of the button
    print(submit_button.is_displayed, submit_button.is_enabled)
    
    submit_button.click()
    driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/div/div[1]/div[2]/form/div[5]/button').click()

    time.sleep(10)
    
    #to refresh the page
    driver.refresh()

    software_test_link = driver.find_element(By.LINK_TEXT, 'Switch to Software Testing')
    software_test_link.click()
    time.sleep(10)
    driver.back()
    time.sleep(10)
    driver.forward()


    driver.close()

   


if __name__ == '__main__':
    main()