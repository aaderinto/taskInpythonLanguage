#run from command line 
#pip install webdriver-manager

#Searching through the web page by elements
print("****************************************************")
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By 

#sub element elements
def locate_by_forms(driver):  
    forms = driver.find_elements(By.TAG_NAME, 'form')
    print("The number of forms is:", len(forms))
    form1 = forms[0]
    email_text = form1.find_element(By.NAME, 'email')
    print(email_text)






def main():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")

    locate_by_forms(driver)
    driver.close()


if __name__ == '__main__':
    main()