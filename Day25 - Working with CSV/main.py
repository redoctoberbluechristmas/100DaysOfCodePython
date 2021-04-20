#with open("weather_data.csv", mode="r") as data_file:
#    data = data_file.readlines()
#    print(data)

#import csv - slicing data with CSV vs. Pandas

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# Get pandas library for data analysis on tabular data

import pandas

# doing typechecks on new library



#data = pandas.read_csv("weather_data.csv")
# print(type(data))   # returns pandas.core.frame.DataFrame (a DataFrame object)
# # Two primary data structures of pandas; Series (1-dimensional) and DataFrame (2-dimensional)
# print(type(data["temp"])) # returns pandas.core.series.Series; similare to a list
# # The column "temp" is a series.

#data_dict = data.to_dict()
#print(data_dict)

# Average a list in conventional way.

# Get data in columns

# print(data["condition"])
# print(data.condition)

# Send series to list
# temps = data["temp"].to_list()
# average = sum(temps) / len(temps)
# print(round(average, 2))

# Use Pandas to get mean.

#mean_temp = data.temp.mean()
#print(round(mean_temp, 2))

# Get ahold of maximum value using data series methods

#max_value = data["temp"].max()
#print(max_value)

# Get data from rows in DataFrame

#monday = data[data.day == "Monday"]   # Within the 'data' DataFrame, and within the column 'day', find rows == to "Monday"
#print(monday)

# Challenge - get row of data where temp was at max

# max_temp = data.temp.max()
# print(type(max_temp))
# print(max_temp)
# # It doesn't like it when you pass max_temp as variable
# print(data[data.temp == max_temp])  #<---doesn't work
# print(data[data.temp == data.temp.max()])  #<--- works

# Convert temp from Celsius to Fahrenheit
# saturday = data[data.day == "Saturday"]
#
# # Convert Saturday temp type to normal value, int
# fahrenheit_temp = int(saturday.temp) * 9 / 5 + 32
# print(fahrenheit_temp)



#data_dict = {
#    "students": ["Amy", "James", "Angela"],
#    "scores": [76, 56, 65]
#}
# Create a dataframe from scratch (not reading from csv)
#data = pandas.DataFrame(data_dict)

# port dict to csv file.
#data.to_csv("new_data.csv")



#################################################
#          SQUIRREL CENSUS                      #
#################################################

# How many gray, black, and cinnamon squirrels?

# 0. Get pandas
import pandas

# 1. Get ahold of data.
squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# 2. Convert CSV into DataFrame.
squirrel_data = pandas.DataFrame(squirrel_data)

# 3. Get "Primary Fur Color" series.

items = squirrel_data["Primary Fur Color"]

# 4. Count the unique values in the series.
num_unique_colors = items.value_counts()

# 5. Output data to csv.
num_unique_colors.to_csv("output.csv")

#################################################
#         END SQUIRREL CENSUS                   #
#################################################

#################################################
#          SQUIRREL CENSUS 2                    #
#################################################

# How many gray, black, and cinnamon squirrels?

# 0. Get pandas
import pandas

# 1. Get ahold of data.
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# 2. Find color counts
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])


# 3. Store color counts in dictionary

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
}

# 4. Convert dictionary to DataFrame

df = pandas.DataFrame(data_dict)

# 5. Output DataFrame to CSV

df.to_csv("output2.csv")

#################################################
#         END SQUIRREL CENSUS                   #
#################################################