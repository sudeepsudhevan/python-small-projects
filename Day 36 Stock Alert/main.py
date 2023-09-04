import requests
from twilio.rest import Client


account_sid = "Your account_sid"  # Twilio account_sid and auth_token
auth_token = "Your Auth_token"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = "Your API KEY"  # Alpha Vantage API KEY

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

NEWS_API_KEY = "Your API"  # NEWS API

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
    # "datatype": "json"

}

response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
stock_data = response.json()
# print(stock_data["Time Series (Daily)"])

closing_stock_price = [value["4. close"] for (date, value) in stock_data["Time Series (Daily)"].items()]
# print(closing_stock_price)

yesterday_close = float(closing_stock_price[0])
day_before_yesterday_close = float(closing_stock_price[1])


price_difference = (yesterday_close - day_before_yesterday_close)
# print(price_difference)

percentage = (price_difference / day_before_yesterday_close) * 100
print(percentage)

pos_percentage = abs(percentage)

if percentage < 0:
    message_head = f"{STOCK_NAME} 🔻{round(pos_percentage)}%\n"
else:
    message_head = f"{STOCK_NAME} 🔺{round(pos_percentage)}%\n"

news_parameters = {
    "q": COMPANY_NAME,
    "apikey": NEWS_API_KEY

}

if pos_percentage > 5:
    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()
    articles = news_data["articles"][:3]
    print(articles)

    news_list = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in articles]

    client = Client(account_sid, auth_token)
    for news in news_list:
        message = client.messages \
            .create(
                body=f"{message_head}{news}",
                from_="+16502623887",  # Your twilio number
                to="Your number"

            )
        print(message.status)


