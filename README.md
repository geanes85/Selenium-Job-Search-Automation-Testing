# Selenium-Job-Search-Automation-Testing
This is a Python-based Selenium test simulating a real job search workflow on Indeed using a Page Object Model, explicit waits, and pytest.

# Job Search Automation

This project demonstrates a basic automated job search test using Selenium WebDriver. The script simulates a user searching for "Junior Python Developer" jobs on Indeed with the "Remote" location.

## Project Structure

- **test_job_search.py**: Contains the test script to run the job search automation.
- **job_search_page.py**: Contains the Page Object Model for the Job Search page.
- **driver_setup.py**: Contains the WebDriver setup and other utilities.
- **requirements.txt**: Dependencies required to run the project.

## How to Run the Test

1. Clone this repository:
   git clone https://github.com/geanes85/Selenium-Job-Search-Automation-Testing.git
2. Install the dependencies:
   pip install -r requirements.txt
3. Run the test:
   python tests/test_job_search.py

# What It Does
-Opens the Indeed homepage.
-Enters "Junior Python Developer" as the job title and "Remote" as the location.
-Validates that the search results contain jobs and include the keyword "Remote".
-Verifies that the page title contains the word "Python".

# Next Steps (for improvement)
-Add more complex assertions (e.g., check if the job title matches).
-Use a headless browser setup for CI/CD pipelines.
-Implement a more advanced Page Object Model for other features on the site.
