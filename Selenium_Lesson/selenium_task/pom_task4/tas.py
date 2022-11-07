from selenium.webdriver.common.by import By

class tas:

    def __init__(self, t):
        t.get("https://academy.testifyltd.com/courses/test-automation-simplified")
        self.success_stories = t.find_element(By.LINK_TEXT, 'Success Stories')
        self.courses = t.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/header/div/div/div[2]/button')
        self.title = t.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/div/div/div[1]/h1')
        self.enrol_now = t.find_element(By.XPATH, '//*[@id="__next"]/main/section[4]/div[1]/div/div[2]/div[2]/div/button')
        self.send_message = t.find_element(By.XPATH, '//*[@id="enrol"]/div/div/div[1]/div/a')