""" 4. Navigate to https://www.bbc.com/  and  print  out  thetop 10 latest news from the home page.
"""


from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 


 
def topTenBBCNews(element):

    #This is to access the url from the browser
    element.get("https://www.bbc.com/")
    
    #This is to maximize the window 
    element.maximize_window()
    #element.implicitly_wait(60)
    
    #This method explicitly waits for the elements to be available and executes immedialtely the element are found.
    web_driver_wait = WebDriverWait(element, 60)
    web_driver_wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'span')))
    
    #This methods gets first 10 the news headlines and terminates
    liveStreams = element.find_elements(By.TAG_NAME, 'span')
    count = 0
    for i in range(len(liveStreams)):
        if(liveStreams[i].get_attribute('aria-hidden') == 'false'):
            count +=1
            if (count <= 10):
                 print(liveStreams[i].text)
            
            
            
   

def main():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    topTenBBCNews(driver)
    driver.close()      

if __name__ == '__main__':
    main()