"""Create a screen and a body head"""
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

coordinates = [x for x in range(0, -41, -20)]
for x in coordinates:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.goto(x, 0)

screen.exitonclick()