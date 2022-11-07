from selenium.webdriver.common.by import By

class contactPage:
    

    def __init__(self, contact):
        contact.get("https://www.testifyltd.com/contact")
        self.firstname = contact.find_element(By.NAME, 'firstname')
