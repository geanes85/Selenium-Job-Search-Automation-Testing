from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.job_search_page import JobSearchPage
import time

from utils.driver_setup import get_driver

def test_job_search():
    driver = get_driver()
    
    try:
        job_search_page = JobSearchPage(driver)

        job_search_page.search_job('Junior Python Developer', 'Remote')

        assert "Python" in driver.title, "Page title doesn't contain 'Python'"
        results = driver.find_elements(By.CLASS_NAME, 'jobsearch-ResultsList')
        assert len(results) > 0, "No job results found"
  
        job_descriptions = driver.page_source
        assert 'Remote' in job_descriptions, "'Remote' not found in job descriptions"
    
    finally:
        driver.quit()

if __name__ == "__main__":
    test_job_search()
