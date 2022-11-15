""" 5. Using any browser navigate to any Youtube video of yourchoice, 
allow your script to wait for the comments to load thenget the first two comments, 
and print them in the terminal.
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 


def scroll_by_offset(action, delta_y):
    action.scroll_by_amount(0, delta_y).perform()


def firstTwoComment(element):
    web_driver_wait = WebDriverWait(element, 60)
    web_driver_wait.until(EC.visibility_of_element_located((By.ID, 'content-text')))  
    comments = element.find_elements(By.ID, 'content-text')
    count = 0
    for i in range(len(comments)):
        count += 1
        if (count <= 2):
             print(comments[i].text)
            
            
            
   

def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.youtube.com/watch?v=aejhNzG5iQs")

    time.sleep(5)

    driver.find_element(By.CSS_SELECTOR, '#content > div.body.style-scope.ytd-consent-bump-v2-lightbox > div.eom-buttons.style-scope.ytd-consent-bump-v2-lightbox > div:nth-child(1) > ytd-button-renderer:nth-child(2) > yt-button-shape > button > yt-touch-feedback-shape > div > div.yt-spec-touch-feedback-shape__fill').click()
    driver.maximize_window()

    time.sleep(5)

    action = ActionChains(driver)
    scroll_by_offset(action, 600)

    firstTwoComment(driver)
    driver.close()
    

    
  

if __name__ == '__main__':
    main()