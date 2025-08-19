import pandas

# DataFrame
data = pandas.read_csv("weather_data.csv")
print(type(data))
data_dict = data.to_dict()
print(data_dict)

# Series
print(type(data["temp"]))
# Note: You can do the above code just with point notation also:
print(type(data.temp))
data_list = data["temp"].to_list()
print(data_list)

# 1. Challenge: Temperatures Average
average_temp = sum(data_list) / len(data_list)
print(average_temp)
average_temp = data["temp"].mean()
print(average_temp)

# 2. Challenge Max and Min temperature
max_temp = data["temp"].max()
min_temp = data["temp"].min()
print(max_temp)
print(min_temp)

# 3. Challenge: Get the row which the highest temp
row_highest_temp = data[data.temp == data["temp"].max()]
print(row_highest_temp)

# Get data in row
monday = data[data["day"] == "Monday"]
print(monday)

# 4. Challenge: Get the monday's temperature and change to Fahrenheit
monday_temp_fahrenheit = (data[data.day == "Monday"]["temp"]).to_list()[0] * 9 / 5 + 32
print(monday_temp_fahrenheit)
# (0 °C × 9/5) + 32 = 32 °F

# DataFrame
data_dict = {
    "students" : ["Samurai", "Leonidas", "Precious"],
    "scores": [90, 90, 100]
}
new_frame = pandas.DataFrame(data_dict)
print(new_frame)
new_csv = pandas.DataFrame(data_dict).to_csv("new_data.csv")
