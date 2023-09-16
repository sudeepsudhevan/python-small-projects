from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome Browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")

# price_dollar = driver.find_element(By.CLASS_NAME, "a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}")


# search_bar = driver.find_element(By.NAME, value="field-keywords")
# print(search_bar.tag_name)
# button = driver.find_element(By.ID, value="nav-search-submit-button")
# print(button.size)
# doc_link = driver.find_element(By.CSS_SELECTOR, ".centerColAlign > div > div > a")
# print(doc_link.text)

# privacy_link = driver.find_element(By.XPATH, value='//*[@id="navFooter"]/div[5]/ul/li[2]/a')
# print(privacy_link.text)

driver.get("https://www.python.org/")
event_time = driver.find_elements(By.CSS_SELECTOR,
                                  value=".event-widget > div > ul > li > time")  # value = ".event-widget time"
event_name = driver.find_elements(By.CSS_SELECTOR, value=".event-widget > div > ul > li > a")

events = {index: {'time': event_time[index].text, 'name': event_name[index].text} for index in range(len(event_time))}
print(events)














# driver.close() close tab
driver.quit()  # close browser


