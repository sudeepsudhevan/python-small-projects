from pprint import pprint
import requests
import os

USER_NAME = os.environ["USER_NAME"]

sheety_data_endpoint = f"https://api.sheety.co/{USER_NAME}/flightDeals/prices"
customers_endpoint = f"https://api.sheety.co/{USER_NAME}/flightDeals/users"

class DataManager:

    def __init__(self):
        self.customer_data = None
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(sheety_data_endpoint)
        response.raise_for_status()
        sheet_data = response.json()
        self.destination_data = sheet_data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            sheety_put_endpoint = f"{sheety_data_endpoint}/{city['id']}"
            response = requests.put(url=sheety_put_endpoint, json=new_data)
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(url=customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
