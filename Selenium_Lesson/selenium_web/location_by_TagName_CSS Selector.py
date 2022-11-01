#run from command line 
#pip install webdriver-manager

#Searching through the web page by elements
print("****************************************************")
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By 

#Locating by id
def locate_by_tagName(driver):  
    first_element = driver.find_element(By.TAG_NAME, 'input')
    print("The first tag element is:", first_element)

    div_elements = driver.find_elements(By.TAG_NAME, 'div')
    print("TotalDiv is", len(div_elements))
    #for div_element in div_elements:
    #          print("The elements with tag name div is: ", div_element)
    


#Locating by name
def locate_by_CSS(driver):
    last_name = driver.find_element(By.CSS_SELECTOR, "#__next > main > section.relative.bg-primary.contact-section > div > div.mt-12.lg\:mt-16.w-full.xl\:w-11\/12.mx-auto.flex.flex-row.flex-wrap.items-start > div.w-full.md\:w-8\/12.bg-white.px-5.md\:px-8.xl\:px-12.pt-12.pb-14 > form > div:nth-child(1) > div:nth-child(2) > input")
    print("The last name element is:", last_name)

    email = driver.find_element(By.CSS_SELECTOR, "#__next > main > section.relative.bg-primary.contact-section > div > div.mt-12.lg\:mt-16.w-full.xl\:w-11\/12.mx-auto.flex.flex-row.flex-wrap.items-start > div.w-full.md\:w-8\/12.bg-white.px-5.md\:px-8.xl\:px-12.pt-12.pb-14 > form > div:nth-child(2) > div:nth-child(1) > input")
    print("The password is: ", email)

    form = driver.find_element(By.XPATH, '/html/body/div/main/section[1]/div/h2')
    print(form.text)

    link = driver.find_element(By.PARTIAL_LINK_TEXT, 'emy')
    print(link.click())

print("****************************************************")

def main():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")

    locate_by_tagName(driver)

    print("****************************************************")

    locate_by_CSS(driver)

    print("****************************************************")


if __name__ == '__main__':
    main()