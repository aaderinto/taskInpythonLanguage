#run from command line 
#pip install webdriver-manager

#Searching through the web page by elements
print("****************************************************")
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 

#Locating by id
def locate_by_id(driver):  
    email_element = driver.find_element(By.ID, 'email')
    print("The email element is:", email_element)

    passwd_element = driver.find_element(By.ID, 'pass')
    print("The password is: ", passwd_element)
    


#Locating by name
def locate_by_name(driver):
    email_name = driver.find_element(By.NAME, 'email')
    print("The email element is:", email_name)

    passwd_name = driver.find_element(By.NAME, 'pass')
    print("The password is: ", passwd_name)


#Locating by class name
def locate_by_className(driver):
    l_creds = driver.find_elements(By.CLASS_NAME, '_6lux')
    for l_cred in l_creds:
        print(l_cred)

def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.facebook.com/")
    locate_by_className(driver)

    print("****************************************************")

    locate_by_id(driver)

    print("****************************************************")

    locate_by_name(driver)


if __name__ == '__main__':
    main()
