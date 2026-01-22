from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class JobSearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.indeed.com"
        self.search_input = (By.ID, "text-input-what")
        self.location_input = (By.ID, "text-input-where")
        self.search_button = (By.CLASS_NAME, "icl-Button")

    def load(self):
        self.driver.get(self.url)

    def search_job(self, job_title, location):
        self.load()

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.search_input))
        
        search_box = self.driver.find_element(*self.search_input)
        search_box.clear()
        search_box.send_keys(job_title)

        location_box = self.driver.find_element(*self.location_input)
        location_box.clear()
        location_box.send_keys(location)

        search_button = self.driver.find_element(*self.search_button)
        search_button.click()
