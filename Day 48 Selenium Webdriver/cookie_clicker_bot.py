from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")

items = driver.find_elements(By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]
print(item_ids)


timeout = time.time() + 5
five_min = time.time() + 60 * 5  # five minutes
while True:
    cookie.click()

    # Every 5 seconds:
    if time.time() > timeout:

        all_prices = driver.find_elements(By.CSS_SELECTOR, value="#store b")

        price_list = []
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                price_list.append(cost)

        # Create dictionary of store items and prices
        cookie_upgrade = {}
        for index in range(len(price_list)):
            cookie_upgrade[price_list[index]] = item_ids[index]

        print(cookie_upgrade)
        # Get current cookie count
        money_element = driver.find_element(By.ID, value="money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        affordable_upgrades = {}
        for cost, value in cookie_upgrade.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = value

        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        # print(highest_price_affordable_upgrade)

        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(By.ID, value=to_purchase_id).click()

        timeout = time.time() + 5

    if time.time() > five_min:
        cookies_per_s = driver.find_element(By.ID, value="cps").text
        print(cookies_per_s)
        break




