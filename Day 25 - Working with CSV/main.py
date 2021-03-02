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



data = pandas.read_csv("weather_data.csv")
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



data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
# Create a dataframe from scratch (not reading from csv)
data = pandas.DataFrame(data_dict)

# port dict to csv file.
data.to_csv("new_data.csv")
