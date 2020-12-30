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

def add_new_country(travel_country, number_visits, travel_cities):

    new_country_dictionary = {}

    new_country_dictionary["country"] = travel_country,
    new_country_dictionary["visits"] = number_visits,
    new_country_dictionary["cities"] = travel_cities,

    #print(new_country_dictionary)

    travel_log.append(new_country_dictionary)
    



#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)



