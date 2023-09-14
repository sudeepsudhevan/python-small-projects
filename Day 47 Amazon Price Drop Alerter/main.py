import requests
from bs4 import BeautifulSoup
# import lxml
import smtplib

MY_EMAIL = "sudeep@gmail.com"
MY_PASSWORD = "Your password"
AMAZON_PRODUCT_LINK = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

# User-agent and Accept language in https://myhttpheader.com/
response = requests.get(AMAZON_PRODUCT_LINK, headers={"User-Agent": "Your user-agent",
                                                      "Accept-Language": "en-US,"})
# print(response.text)
amazon_web_page_link = response.text
soup = BeautifulSoup(amazon_web_page_link, "html.parser")
price_tag = soup.find(name="span", class_="a-offscreen")
price = price_tag.getText()
# print(price.split("$")[1])
price_as_float = float(price.split("$")[1])
print(price_as_float)

title = soup.find(id="productTitle").getText().strip()
print(title)

if price_as_float < 100:
    message = f"{title} is now {price}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{AMAZON_PRODUCT_LINK}".encode("utf-8")
        )
