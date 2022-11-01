#run from command line 
#pip install webdriver-manager

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def main():
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    driver.get("https://www.google.co.uk/")
    driver.close()

main()