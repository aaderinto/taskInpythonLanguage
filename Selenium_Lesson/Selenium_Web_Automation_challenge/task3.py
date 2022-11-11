""" 3. Navigate any browser to https://weather.com/ get thecurrent  temperature  and  print  it  out  in  the  terminal.  
Thenprint out the temperature for Morning, Afternoon, Evening,and Overnight.
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 


 
def currentTemperature(element):
    element.get("https://weather.com/")
    #element.delete_all_cookies()
    element.maximize_window()
    element.implicitly_wait(60)
    element.find_element(By.CSS_SELECTOR, '#truste-consent-button').click()
    Temp = element.find_element(By.CSS_SELECTOR, '#WxuSavedLocations-header-9aea3e61-fbf8-4da4-9e07-f96abf18cdf1 > div > div > div > div.styles--cards--39bdo.styles--cardCarousel--Yl375 > div > div > div > a.styles--weatherData--24HO9.weather-data.Button--default--2gfm1 > span')
    print("The Current Temperature is ",Temp.text)
    Temp.click()
    time.sleep(20)

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