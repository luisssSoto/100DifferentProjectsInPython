"""Reading a CSV (Comma Separated Value) File"""

# 1. traditional way
with open("weather_data.csv", "r") as weather_file:
    data = weather_file.readlines()
print(data)

# 2. built-in module
import csv
with open("weather_data.csv", "r") as weather_file:
    data = csv.reader(weather_file)
    temperatures = []
    for row in data:
        if row[1].isdigit():
            temperatures.append(int(row[1]))
print(temperatures)

# 3. external module pandas
import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(data.head())
print(data.describe())
print(data["temp"])