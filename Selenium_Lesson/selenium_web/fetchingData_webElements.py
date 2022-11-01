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
def print_webAttributes(attribute):
    print("ID", attribute.get_attribute('id'))
    print("Class", attribute.get_attribute('class'))
    print("Style", attribute.get_attribute('style'))
    print("INNER HTML", attribute.get_attribute('innerHTML'))
    print("INNER TEXT", attribute.get_attribute('innerText'))
    print("TYPE"), attribute.get_attribute('type')
    print("HREF"), attribute.get_attribute('href')


#Getting the property of a web element on a web page
def locate_web_element_properties(e):
    e.click()
    print("Check State", e.get_property("checked"))


def main():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    element = driver.find_element(By.TAG_NAME, 'textarea')
    attribute = driver.find_element(By.LINK_TEXT, 'Academy')
    property_partner = driver.find_element(By.ID, "Partnership")
    property_hiring = driver.find_element(By.ID, "Hiring")
    property_training = driver.find_element(By.ID, "Training")
    property_GE = driver.find_element(By.ID, "General Enquiry")

    print_elements(element)

    print("****************************************/t")

    print_webAttributes(attribute)

    print("****************************************/t")

    locate_web_element_properties(property_partner)
    locate_web_element_properties(property_training)
    locate_web_element_properties(property_hiring)
    locate_web_element_properties(property_GE)



    print("****************************************/t")
    driver.close()


if __name__ == '__main__':
    main()