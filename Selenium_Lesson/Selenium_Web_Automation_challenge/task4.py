""" 4. Navigate to https://www.bbc.com/  and  print  out  thetop 10 latest news from the home page.
"""


from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By 


 
def topTenBBCNews(element):
    element.get("https://www.bbc.com/")
    #element.delete_all_cookies()
    element.maximize_window()
    element.implicitly_wait(60)
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