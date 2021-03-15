import pandas


# Goals - Take csv of NATO phonetic alphabet and:
# 1. Create a dictionary in this format: {"A": "Alpha"}  convert CSV into dictionary. Use dictionary comprehension
# 2. Create a list of phonetic codewords froma  word that user inputs.
# {new_key:new_value for (index, row) in data.iterrows()}

data = pandas.read_csv("nato_phonetic_alphabet.csv")

data_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(data_dict)

user_input = input("Enter a word.").upper() # User should get a list of NATO alphabet equivalents.
# Use a list comprehension to check elements of word against keys in dictionary.
# for each letter in user_input, look-up its value in data_dict and output that to input_list.

input_list = [data_dict[letter] for letter in user_input]
print(input_list)

# I am able to use "letter" because "letter" is the dictionary key.
#for letter in user_input:
 #   print(data_dict[letter])


#result = [ ]