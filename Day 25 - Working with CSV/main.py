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

data = pandas.read_csv("weather_data.csv")
print(data["temp"])
