from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import html
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)


FORM_URL = ("https://docs.google.com/forms/d/e/1FAIpQLSf3qbYeUhqpKEVpmshS0t7bp3MSd9vOwjf1DSBsiXLAjlTfw/viewform?usp"
            "=sf_link")

ZILLOW_URL = ("https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C"
              "%22mapBounds%22%3A%7B%22north%22%3A37.9054342393378%2C%22east%22%3A-122.22184268359375%2C%22south%22"
              "%3A37.64492017286698%2C%22west%22%3A-122.64481631640625%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22"
              "%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22"
              "%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B"
              "%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C"
              "%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B"
              "%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22"
              "%3A20330%2C%22regionType%22%3A6%7D%5D%7D")

response = requests.get(ZILLOW_URL, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0",
    "Accept-Language": "en-US,en;q=0.5",
})
zillow_website = response.text
# print(zillow_website)

soup = BeautifulSoup(zillow_website, "html.parser")

address_list = [address.getText().split("|")[-1] for address in soup.select(selector="article address")]
print(address_list)


links = soup.select(selector="article a")
all_links = []
for link in links:
    href = link["href"]
    # print(href)
    if "http" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)

print(all_links)


prices = soup.select(selector="article div span")
all_prices = [price.get_text().split("+")[0] for price in prices if "$" in price.text]
print(all_prices)


for n in range(len(all_links)):
    driver.get(FORM_URL)

    time.sleep(2)
    address = driver.find_element(By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    address.send_keys(address_list[n])
    price.send_keys(all_prices[n])
    link.send_keys(all_links[n])
    submit_button.click()
