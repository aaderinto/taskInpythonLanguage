#run from command line 
#pip install webdriver-manager

#Searching through the web page by the path name

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 



def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/")
    
    #Locating by tag name
    tag_element = driver.find_element(By.TAG_NAME, 'h1')
    print("The tag name for the welcome page intro is:", tag_element, tag_element.text)
    
    print("/n ******************************* /n")

    #locating by class name
    class_element = driver.find_element(By.CLASS_NAME, 'react-reveal')
    print("The tag name for the welcome page intro is:", class_element, class_element.text)

    print("/n ******************************* /n")

    #locating by XPATH
    xpath_element = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/div/div[1]/div[1]/h1')
    print("The tag name for the welcome page intro is:", xpath_element, xpath_element.text)



main()