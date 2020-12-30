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

