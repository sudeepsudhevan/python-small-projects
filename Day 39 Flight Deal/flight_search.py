import requests
from flight_data import FlightData

TEQUILA_ENDPOINT = "Your TEQUILA_ENDPOINT"
TEQUILA_API_KEY = "Your TEQUILA_API_KEY"


class FlightSearch:

    def get_destinaion_code(self, city_name):
        query = {
            "term": city_name,
            "location_types": "city"
        }
        header = {
            "apikey": TEQUILA_API_KEY,
            # "accept": "application/json"
        }

        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"

        response = requests.get(url=location_endpoint, params=query, headers=header)
        response.raise_for_status()
        data = response.json()["locations"]
        code = data[0]["code"]
        return code

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
            print(f"No flights found for {destination_city_code}.")
            return None

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