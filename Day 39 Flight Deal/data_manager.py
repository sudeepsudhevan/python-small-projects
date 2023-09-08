from pprint import pprint
import requests

sheety_data_endpoint = "Your data End point"


class DataManager:

    def __init__(self):
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
