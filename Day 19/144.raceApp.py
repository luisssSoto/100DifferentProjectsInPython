"""Turtle Race"""
"""Coordinate System Turtle"""
from turtle import Turtle, Screen
from random import randint

turtle_colors = ["blue", "red", "yellow", "orange", "green", "purple"]
turtle_names = ["blue", "red", "yellow", "orange", "green", "purple"]
turtle_objs = []

my_screen = Screen()
my_screen.setup(width=500, height=400)
is_race_on = False
user_bet = my_screen.textinput(title="Make your bet", prompt="Which turtle would you like to bet? ")
print(f"user's bet: {user_bet}")

def creating_turtles(names, colors ):
    index = 0
    x = -230
    y = -80
    for turtle in names:
        turtle = Turtle("turtle")
        turtle.color(colors[index])
        turtle.speed("fastest")
        turtle.penup()
        turtle.goto(x, y)
        index += 1
        y += 40
        turtle_objs.append(turtle)

creating_turtles(turtle_names, turtle_colors)
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_objs:
        distance = randint(1, 10)
        turtle.forward(distance)
        if turtle.xcor() >= 230:
            is_race_on = False
            if user_bet == turtle.pencolor():
                print(f"You've won, the {turtle.pencolor()} is the winner!")
            else:
                print(f"You've lost, the {turtle.pencolor()} is the winner!")

my_screen.exitonclick()