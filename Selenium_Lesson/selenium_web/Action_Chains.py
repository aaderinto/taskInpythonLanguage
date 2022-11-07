#run from command line 
#pip install webdriver-manager

#Searching through the web page by elements
print("****************************************************")
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains 

#Send keys method
def scroll_to_element(action, element):
    action.move_to_element(element).perform()

def scroll_by_offset(action, delta_y):
    action.scroll_by_amount(0, delta_y).perform()

def right_click_context(action, element):
    scroll_to_element(action, element)
    action.context_click(element).perform()

def highlight_element1(action, element, limit=15):
    action.drag_and_drop_byoffset(element, 0, limit)
    action.perform()

def highlight_element2(action, element, limit=15):
    action.move_to_element(element)
    action.move_to_offset(0, 10)
    action.click_and_hold(on_element = None)
    action.move_by_offset(0, 20)
    action.release(on_element = None)
    action.perform()

def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    action = ActionChains(driver)
    #scroll_to_element(action, driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[3]'))
    scroll_by_offset(action, 100)
    time.sleep(10)
    scroll_by_offset(action, -50)
    driver.close()

   


if __name__ == '__main__':
    main()