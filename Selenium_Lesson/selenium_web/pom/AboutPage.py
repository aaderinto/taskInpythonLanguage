from selenium.webdriver.common.by import By

class aboutPage:
    

    def __init__(self, about):
        about.get("https://www.testifyltd.com/about")
        self.title = about.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/div[1]/div/div/div/h1')
