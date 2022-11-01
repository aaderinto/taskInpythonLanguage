""" Navigate to the website https://academy.testifyltd.com/

Get the element with the text "© 2022 Testify Limited. All rights reserved."

Print out the element text, and properties, and it attributes """


#run from command line 
#pip install webdriver-manager

#Searching through the web page by elements
print("****************************************************")
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


#Printing Elements
def print_elements(element):  
    print("ID: ",element.id)
    print("text", element.text)
    print("location", element.location)
    print("TAG Name", element.tag_name)
    print("Size", element.size)
    #print("Accessible Name", element.aria_role)
    print("Rectangle", element.rect)

#Printing Web Element Attributes
def print_webAttributes(element):
    print("ID", element.get_attribute('id'))
    print("Class", element.get_attribute('class'))
    print("Style", element.get_attribute('style'))
    print("INNER HTML", element.get_attribute('innerHTML'))
    print("INNER TEXT", element.get_attribute('innerText'))
    print("TYPE"), element.get_attribute('type')
    print("HREF"), element.get_attribute('href')


#Getting the property of a web element on a web page
def locate_web_element_properties(element):
    print("Class Property", element.get_property("class"))
    print("Length of Text Property", element.get_property("text_length"))


def main():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get("https://academy.testifyltd.com/")
    element = driver.find_element(By.XPATH, '//*[@id="__next"]/section/div/div[2]/div[2]')
    
    

    print_elements(element)

    print("****************************************/t")

    print_webAttributes(element)

    print("****************************************/t")

    locate_web_element_properties(element)
    



    print("****************************************/t")
    driver.close()


if __name__ == '__main__':
    main()