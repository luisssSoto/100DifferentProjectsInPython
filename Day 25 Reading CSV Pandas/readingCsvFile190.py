"""Reading a CSV (Comma Separated Value) File"""
from os import getenv
from dotenv import load_dotenv

load_dotenv()
root = getenv('ROOT')
print(f"root: {root} and type: {type(root)}")

# 1. traditional way
with open(f"{root}weather_data.csv", "r") as weather_file:
    data = weather_file.readlines()
print(data, end='\n')

# 2. built-in module
import csv
with open(f"{root}weather_data.csv", "r") as weather_file:
    data = csv.reader(weather_file)
    temperatures = []
    for col in data:
        if col[1].isdigit():
            temperatures.append(int(col[1]))
print(temperatures, end='\n')

# 3. external module pandas
import pandas

data = pandas.read_csv(f"{root}weather_data.csv")
print(data)
print(data.head())
print(data.describe())
print(data["temp"])