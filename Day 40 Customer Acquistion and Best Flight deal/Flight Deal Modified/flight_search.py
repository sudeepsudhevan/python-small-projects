import requests
from flight_data import FlightData
import os

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_API_KEY = os.environ["TEQUILA_API_KEY"]


class FlightSearch:

    def __init__(self):
        self.city_codes = []

    def get_destinaion_code(self, city_name):
        header = {
            "apikey": TEQUILA_API_KEY,
            # "accept": "application/json"
        }
        print("get destination codes triggered")
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        for city in city_name:
            query = {
                "term": city,
                "location_types": "city"
            }
            response = requests.get(url=location_endpoint, params=query, headers=header)
            response.raise_for_status()
            data = response.json()["locations"]
            code = data[0]["code"]
            self.city_codes.append(code)

        return self.city_codes

    def check_flights(self, origin_city, destination_city_code, from_time, to_time):
        query = {
            "fly_from": origin_city,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"

        }
        header = {
            "apikey": TEQUILA_API_KEY,
        }

        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search",
                                headers=header,
                                params=query
                                )
        try:
            data = response.json()["data"][0]
        except IndexError:

            query["max_stopovers"] = 1
            response = requests.get(
                url=f"{TEQUILA_ENDPOINT}/v2/search",
                headers=header,
                params=query
            )
            try:
                data = response.json()["data"][0]
            except IndexError:
                print(f"There is no fight in {destination_city_code}")
                return None
            else:
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][0]["cityTo"],
                    destination_airport=data["route"][0]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][2]["local_departure"].split("T")[0],
                    stop_overs=1,
                    via_city=data["route"][0]["cityTo"]
                )
                return flight_data
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            print(f"{flight_data.destination_city}: £{flight_data.price}")
            return flight_data
