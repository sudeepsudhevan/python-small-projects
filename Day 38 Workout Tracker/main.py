import requests
import datetime as dt
import os

# nutritionix api and app id
API_KEY = os.environ["NAT_API_KEY"]  # Your nutritionix api key
APP_ID = os.environ["NAT_APP_ID"]  # Your nutritionix app id

sheet_endpoint = os.environ["SHEET_ENDPOINT"]  # your sheety endpoint

GENDER = "male"
WEIGHT_KG = 54
HEIGHT_CM = 160
AGE = 24

exercise_text = input("Tell me which exercise you did: ")

exercise_parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(exercise_endpoint, json=exercise_parameters, headers=headers)
response.raise_for_status()
result = response.json()
# print(result)

today_date = dt.datetime.now().strftime("%d/%m/%Y")
now_time = dt.datetime.now().strftime("%X")


for exercise in result["exercises"]:
    sheet_input = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],


        }
    }

    bearer_headers = {
        "Authorization": f"Bearer {os.environ['SHEETY_TOKEN']}"  # Your sheety token (bearer)
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_input, headers=bearer_headers)
    print(sheet_response.text)

