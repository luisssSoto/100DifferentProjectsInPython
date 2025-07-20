"""Coordinate System Turtle"""
from turtle import Turtle, Screen

turtle_colors = ["blue", "red", "yellow", "orange", "green", "purple"]
turtle_names = ["blue", "red", "yellow", "orange", "green", "purple"]

my_screen = Screen()
my_screen.setup(width=500, height=400)
user_bet = my_screen.textinput(title="Make your bet", prompt="Which turtle would you like to bet? ")
print(f"user's bet: {user_bet}")

def creating_turtles(names, colors ):
    index = 0
    x = -230
    y = -80
    for turtle in names:
        turtle = Turtle("turtle")
        turtle.color(colors[index])
        turtle.penup()
        turtle.goto(x, y)
        index += 1
        y += 40

creating_turtles(turtle_names, turtle_colors)
my_screen.exitonclick()