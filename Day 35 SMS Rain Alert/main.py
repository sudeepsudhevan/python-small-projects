import requests
# import os
from twilio.rest import Client

open_W_endpoint = "https://api.openweathermap.org/data/2.8/onecall"
api_key = "Your open weather Api"

account_sid = 'Your twilio account_sid'
auth_token = 'your auth token'

MY_LAT = 55.519551
MY_LONG = 80.299364

weather_parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(open_W_endpoint, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()

# condition_code_list = [weather_data["hourly"][index]["weather"][0]["id"] for index in range(12)]
# print(condition_code_list)

weather_slice = weather_data["hourly"][:12]  # slicing
print(weather_slice)

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an umbrella",
            from_='+16502623897',
            to='+917994258774'
        )
    print(message.status)
