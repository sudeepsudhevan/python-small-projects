from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import time, sleep
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

FB_MAIL = "@gmail.com"
FB_PASSWORD = ""

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com/")

# login button

sleep(10)
login_button = driver.find_element(By.XPATH, value='//div[text()="Log in"]')
login_button.click()

# Facebook
input("facebook")
sleep(2)
fb_button = driver.find_element(By.XPATH, value='//div[text()="Log in with Facebook"]')
fb_button.click()

base_window = driver.window_handles[0]
fb_window = driver.window_handles[1]
driver.switch_to.window(fb_window)

sleep(2)
email_input = driver.find_element(By.NAME, value="email")
email_input.send_keys(FB_MAIL)

password_input = driver.find_element(By.NAME, value="pass")
password_input.send_keys(FB_PASSWORD)

fb_login = driver.find_element(By.NAME, value="login")
fb_login.click()

driver.switch_to.window(base_window)

print(driver.title)
sleep(10)

allow_location = driver.find_element(By.XPATH, value='//div[text()="Allow"]')
allow_location.click()

notification_button = driver.find_element(By.XPATH, value='//div[text()="Not interested"]')
notification_button.click()

# cookie= driver.find_element(By.XPATH, value='//div[text()=""]')
sleep(15)
for n in range(100):

    sleep(3)

    try:
        print("called")
        like_button = driver.find_element(By.XPATH,
                                          value='//*[@id="c-1445344539"]/div/div[1]/div/div/main/div/div/div[1]/div/div[4]/div/div[4]/button')
        like_button.click()

    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()

        except NoSuchElementException:
            sleep(2)

driver.quit()
