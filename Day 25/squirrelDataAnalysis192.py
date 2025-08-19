import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250815.csv")

squirrel_color_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [0, 0, 0],
}

squirrel_colors = data["Primary Fur Color"].to_list()
for color in squirrel_colors:
    if color == "Gray":
        squirrel_color_dict["Count"][0] += 1
    elif color == "Cinnamon":
        squirrel_color_dict["Count"][1] += 1
    elif color == "Black":
        squirrel_color_dict["Count"][2] += 1

print(squirrel_color_dict)
squirrel_color_count = pandas.DataFrame(squirrel_color_dict).to_csv("squirrel_color_count.csv")


