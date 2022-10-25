from lib2to3.pgen2 import driver
from time import sleep
from selenium import webdriver

def main():
    driver = webdriver.Chrome(executable_path="/Users/adetomiwaaderinto/Desktop/Webdrivers/chromedriver")
    driver.get("https://www.google.co.uk/")
    sleep(10)
    driver.close()

main()