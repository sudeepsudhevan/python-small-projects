from selenium import webdriver
from selenium.webdriver.common.by import By

import time

EMAIL = "@gmail.com"
PASSWORD = ""

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location"
           "=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

# Sign in
sign_in_link = driver.find_element(By.LINK_TEXT, value="Sign in")
sign_in_link.click()

# EMAIL
email_input = driver.find_element(By.ID, value="username")
email_input.send_keys(EMAIL)

# PASSWORD
password_input = driver.find_element(By.ID, value="password")
password_input.send_keys(PASSWORD)

# submit button
submit_button = driver.find_element(By.CSS_SELECTOR, value=".login__form_action_container button")
submit_button.click()

# jobs_list

all_jobs = driver.find_elements(By.CLASS_NAME, value="job-card-container--clickable")
for job in all_jobs:
    job.click()
    # job save button
    time.sleep(2)
    job_save = driver.find_element(By.CLASS_NAME, value=".jobs-save-button")
    job_save.click()
