import requests
import datetime as dt

################################## Create a Username ####################################

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "Your Pixe.la token"
USERNAME = "Your user_name"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

################################## Create a Graph ##########################################

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

############################ Enter data in pixel ###################################

today_date = dt.datetime.now()

pixel_entry_data = {
    "date": today_date.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today? "),

}

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

response = requests.post(url=pixel_creation_endpoint, json=pixel_entry_data, headers=headers)
print(response.text)


############################# Updating the pixel data #############################################

date = dt.datetime(year=2023, month=9, day=4)
updating_date = date.strftime("%Y%m%d")

update_data = {
    "quantity": "12",
}

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{updating_date}"

# response = requests.put(url=update_endpoint, json=update_data, headers=headers)
# print(response.text)


################################ Delete a pixel data ##########################################

date = dt.datetime(year=2023, month=9, day=4)
deleting_date = date.strftime("%Y%m%d")

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{deleting_date}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
