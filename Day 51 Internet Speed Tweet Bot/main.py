from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait

TWITTER_EMAIL = "@gmail.com"
TWITTER_PASSWORD = ""
USER_NAME = ""

PROMISED_DOWN = 15
PROMISED_UP = 5


class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(url="https://www.speedtest.net/")

        # sleep(4)
        # accept_cookies = self.driver.find_element(By.CLASS_NAME, value="onetrust-banner-options")
        # accept_cookies.click()

        sleep(5)
        go_button = self.driver.find_element(By.CLASS_NAME, value="start-text")
        go_button.click()

        sleep(100)
        self.down = self.driver.find_element(By.CLASS_NAME, value="download-speed").text
        self.up = self.driver.find_element(By.CLASS_NAME, value="upload-speed").text
        print(self.down)
        print(self.up)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login")

        sleep(15)
        email = self.driver.find_element(By.NAME, value="text")
        email.send_keys(TWITTER_EMAIL)
        sleep(2)
        email.send_keys(Keys.ENTER)

        # sleep(2)
        # user_name = self.driver.find_element(By.NAME, value="text")
        # user_name.send_keys(USER_NAME)
        # user_name.send_keys(Keys.ENTER)

        sleep(2)
        password = self.driver.find_element(By.NAME, value="password")
        password.send_keys(TWITTER_PASSWORD)
        sleep(2)
        password.send_keys(Keys.ENTER)

        sleep(5)
        tweet_compose = self.driver.find_element(By.CSS_SELECTOR, value='br[data-text="true"]')

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        sleep(3)

        tweet_button = self.driver.find_element(By.XPATH,
                                                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div['
                                                '3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div['
                                                '2]/div[3]/div/span/span')
        tweet_button.click()

        sleep(2)
        self.driver.quit()
