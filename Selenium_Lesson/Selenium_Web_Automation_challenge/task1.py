"""Navigate to the website https://www.facebook.com/

Find the email box and enter an email value

Find the password box and enter a password value

Find the Login button and click it"""
print("****************************************************")
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait #the import line that allows the wait of 20secs
from selenium.webdriver.support import expected_conditions as EC

 

#Send keys method
def enter_value_to_text_field(element, *value):
    element.send_keys(value)

def clickable_method(element):
    web_driver_wait = WebDriverWait(element, 20) #waits 20sec for the element
    web_driver_wait.until(EC.element_to_be_clickable((By.NAME,'login'))) #checks if the element is clickable for 20secs
    #element.find_element(By.NAME,'login').click()
    button = element.find_element(By.NAME,'login')
    element.execute_script("arguments[0].click();", button)
    time.sleep(10)




def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.facebook.com/")

    enter_value_to_text_field(driver.find_element(By.XPATH, '//*[@id="email"]'), 'longeurpadi@yahoo.com')
    enter_value_to_text_field(driver.find_element(By.ID, 'pass'), 'Ikeade_123@')

    
    clickable_method(driver)
  

   


if __name__ == '__main__':
    main()