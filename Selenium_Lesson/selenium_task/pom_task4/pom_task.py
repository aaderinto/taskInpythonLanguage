"""Create a page object model for this page https://academy.testifyltd.com/courses/test-automation-simplified

Create another object model for this page https://academy.testifyltd.com/courses/switch-to-software-testing"""
#POM: Page Object Model

print("****************************************************")
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from tas import tas
from sts import sts



def main():
    print("*******Output for Test Automation*********")

    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    """ tas_t = tas(driver)
    print(tas_t.success_stories.text,"************", tas_t.title.text)
    tas_t.courses.click()
    driver.back()
    tas_t.enrol_now.click()
    time.sleep(5)
    tas_t.send_message.click()
    driver.back()
    time.sleep(10) """


    print("*******Output for Switch to Software Testing*********")

    sts_t = sts(driver)
    """  print(sts_t.success_stories.text,"************", sts_t.title.text)
    sts_t.courses.click()
    driver.back() """
    sts_t.enrol_now.click()
    time.sleep(10)
    sts_t.testimony.click()
    driver.back()
    time.sleep(10)
    

 

    driver.close()


if __name__ == '__main__':
    main()