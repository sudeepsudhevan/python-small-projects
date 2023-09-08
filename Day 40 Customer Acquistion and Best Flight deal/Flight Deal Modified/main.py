from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "LON"

# print(sheet_data)
if sheet_data[0]["iataCode"] == "":
    city_names = [row["city"] for row in sheet_data]

    data_manager.city_codes = flight_search.get_destinaion_code(city_names)
    data_manager.update_destination_codes()
    sheet_data = data_manager.get_destination_data()

destinations = {
    data["iataCode"]: {"id": data["id"], "city": data["city"], "price": data["lowestPrice"]} for data in sheet_data}

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=6 * 30)

for destination in destinations:
    flight = flight_search.check_flights(
        origin_city=ORIGIN_CITY_IATA,
        destination_city_code=destination,
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    if flight is None:
        continue

    print(flight.price)

    if flight.price < destinations[destination]["price"]:

        users = data_manager.get_customer_emails()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]

        message = (f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} "
                   f"to {flight.destination_city}-{flight.destination_airport}, "
                   f"from {flight.out_date} to {flight.return_date}.")

        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

        notification_manager.send_emails(emails, message)
