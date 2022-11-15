""" 3. Navigate any browser to https://weather.com/ get thecurrent  temperature  and  print  it  out  in  the  terminal.  
Thenprint out the temperature for Morning, Afternoon, Evening,and Overnight.
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



 
def currentTemperature(element):

    element.get("https://weather.com/")

    element.maximize_window()

    web_driver_wait = WebDriverWait(element, 60)
    web_driver_wait.until(EC.visibility_of_element_located((By.ID, 'truste-consent-button')))

    element.find_element(By.ID, 'truste-consent-button').click()

    web_driver_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[class='styles--temperature--3YaGV']")))
    tempHome = element.find_element(By.CSS_SELECTOR, "[class='styles--temperature--3YaGV']")

    print("The Current Temperature is ",tempHome.text)

    tempHome.click()
    time.sleep(5)

    web_driver_wait.until(EC.visibility_of_any_elements_located((By.TAG_NAME, 'li')))

    allTemp = element.find_elements(By.TAG_NAME, 'div')

    count = 0
    Days = ['Morning', 'Afternoon', 'Evening','OverNight']
    for i in range(len(allTemp)):
        if((allTemp[i].get_attribute('data-testid') == 'SegmentHighTemp') and (allTemp[i].find_element(By.TAG_NAME,'span').get_attribute('data-testid') == 'TemperatureValue')):
            count +=1
            if (count <= 4):
                print("The " +  Days[count-1] + " Temperature is " + allTemp[i].text)  


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    currentTemperature(driver)
    driver.close()
    

    
  

if __name__ == '__main__':
    main()