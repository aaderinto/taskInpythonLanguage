""" 5. Using any browser navigate to any Youtube video of yourchoice, 
allow your script to wait for the comments to load thenget the first two comments, 
and print them in the terminal.

"""


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 


 
def firstTwoComment(element):
    #element.delete_all_cookies()
    element.maximize_window()
    element.implicitly_wait(60)
    element.find_element(By.CSS_SELECTOR, '#content > div.body.style-scope.ytd-consent-bump-v2-lightbox > div.eom-buttons.style-scope.ytd-consent-bump-v2-lightbox > div:nth-child(1) > ytd-button-renderer:nth-child(2) > yt-button-shape > button > yt-touch-feedback-shape > div > div.yt-spec-touch-feedback-shape__fill').click()
    comments = element.find_elements(By.ID, 'content-text')
    #count = 0
    for i in range(len(comments)):
        print(comments[i].text)
            
            
            
   

def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.youtube.com/watch?v=aejhNzG5iQs")
    firstTwoComment(driver)
    driver.close()
    

    
  

if __name__ == '__main__':
    main()