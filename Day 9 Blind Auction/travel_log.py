travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country_visited,no_of_visits,cities_names):
    new_country = {}
    new_country["country"] = country_visited           # add element to dictionary
    new_country["visits"] = no_of_visits
    new_country["cities"] = cities_names

    travel_log.append(new_country)                      # add a dictionary to the list

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
