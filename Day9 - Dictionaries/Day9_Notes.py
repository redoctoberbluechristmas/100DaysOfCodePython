programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again."
}

#Referencing a dictionary entry

print(programming_dictionary["Bug"])


#Adding a new dictionary entry

programming_dictionary["Loop"] = "The action of doing something over and over again."


print(programming_dictionary)


# Create an empty dictionary

empty_list = []
empty_dictionary = {}

# Wipe an existing dictionary

empty_dictionary = {}   #Same as creating an empty one.


# Edit a current entry, redefining the value of the key bug.

programming_dictionary["Bug"] = "bug bug bug"


# Iterate through dictionary

## Print only Keys
for key in programming_dictionary:
    print(key)
    # Retrive values
    print(programming_dictionary[key])



# Nesting Lists and Dictionaries

{
    Key: [List]
    Key2: {Dictionary}
}


# In dictionary, each key can only have one value. If you want Key to have multiple values, you need a list

france_cities = ["Paris", "Cherbourg", "Dijon"]

cities_i_have_been_to = {
    "France": [france_cities]
}

cities_i_have_been_to = {
    "France": ["Paris", "Cherbourg", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

print(cities_i_have_been_to["France"])
print(cities_i_have_been_to["Germany"[0]])

## Nested dictionaries
## travel_log is a dictionary, with country names as its Keys.
## Each country name Key has a dictionary as its value, with the nested keys being things like cities_visited, and total_visits.
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"],"total_visits": 12,},
    "Germany": {
        "cities_visited": [
            "Berlin", 
            "Stuttgart", 
            "Munich"
        ],
        "total_visits": 1,
        ]
    }
}

# Nesting a dictionary inside a list
# Instead of one dictionary, travel_log is a list. Each entry in the list is a dictionary, representing a country.

travel_log = [
    {
        "country": "France", 
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Stuttgart", "Munich"],
        "total_visits": 1
    }
]

# Now, we can add as many dictionaries to the list we want.