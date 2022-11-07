from selenium.webdriver.common.by import By

class sts:

    def __init__(self, t):
        t.get("https://academy.testifyltd.com/courses/switch-to-software-testing")
        self.success_stories = t.find_element(By.LINK_TEXT, 'Success Stories')
        self.courses = t.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/header/div/div/div[2]/button')
        self.title = t.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/div/div/div[1]/h1')
        self.enrol_now = t.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/div/div/div[1]/div/button')
        self.testimony = t.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/div/div/div[2]/div/button[1]')