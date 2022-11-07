#POM: Page Object Model
#run from command line 
#pip install webdriver-manager

#Searching through the web page by elements
print("****************************************************")
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from AboutPage import aboutPage
from contactUsPage import contactPage



def main():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    page_title = aboutPage(driver)
    print(page_title.title.text)
    time.sleep(10)
    

    contactForm = contactPage(driver)
    print(contactForm.firstname.send_keys('Adetomiwa'))
    time.sleep(10)

    driver.close()


if __name__ == '__main__':
    main()