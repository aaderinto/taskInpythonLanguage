  # Using    the    firefox    browser    
  # navigate    tohttps://www.google.com/  
  # enter  the  text  Python  in  thesearch  box,  
  # then  send  the  Enter  key.  
  # Get  the  text  from  theWikipedia  brief  on  the  right  side  
  # and  print  the  value  in  theconsole.

from selenium import webdriver
import time
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait #the import line that allows the wait of 20secs
from selenium.webdriver.support import expected_conditions as EC

 

#Send keys method
def enter_value_to_google_text_field(element, *value):
    element.get("https://www.google.com/")
    element.maximize_window()
    element.find_element(By.CSS_SELECTOR, '#L2AGLb > div:nth-child(1)').click()
    search_text_box = element.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    time.sleep(7)
    search_text_box.click()
    element.implicitly_wait(3)
    search_text_box.send_keys('Python')
    button = element.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]')
    element.execute_script("arguments[0].click();", button)

    



def get_info(element):
    element.get("https://www.google.com/search?q=Python&oq=python&aqs=chrome.0.69i59j0i433i512j0i131i433i512l2j69i65j69i60l3.2796j0j7&sourceid=chrome&ie=UTF-8")
    header = element.find_element(By.CSS_SELECTOR, '.SPZz6b')
    result = element.find_element(By.CSS_SELECTOR, '.kno-rdesc')

    print("\n", header.text, "\n\n",  result.text)
    
    
    



def main():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    enter_value_to_google_text_field(driver, 'Python')
    get_info(driver)
    driver.close()
    

    
  

if __name__ == '__main__':
    main()