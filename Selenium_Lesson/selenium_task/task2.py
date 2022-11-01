"""Visit the website https://academy.testifyltd.com/

Locate the button with the text "Explore Courses" and print out the element

Locate the element with the text "Subscribe to receive training updates from Testify" and print it."""""


#run from command line 
#pip install webdriver-manager

#Searching through the web page by elements
print("****************************************************")
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


#Printing Elements
def print_explore_button(element):
    print("ID: ", element.id)
    print("Text", element.text)
        
    

#Printing Web Element Attributes
def print_text(elem):
    print("ID: ", elem.id)
    print("Tag Name", elem.tag_name)
    print("location", elem.location)
    print("Size", elem.size)
    print("Rectangle", elem.rect)
    




def main():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get("https://academy.testifyltd.com/")
    element = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/div/div/div[1]/div/button/span[1]')
    elem = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[11]/div/div/div[1]/h2')

    
    

    print_explore_button(element)

    print("****************************************/t")

    print_text(elem)

  
    



    print("****************************************/t")
    driver.close()


if __name__ == '__main__':
    main()