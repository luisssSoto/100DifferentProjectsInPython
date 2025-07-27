"""Create a screen and a body head"""
from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

segments = []
coordinates = [x for x in range(0, -41, -20)]

for x in coordinates:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(x, 0)
    segments.append(new_segment)

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    for new_segment in range(len(segments) - 1, 0, -1):
        new_x = segments[new_segment - 1].xcor()
        new_y = segments[new_segment -1].ycor()
        segments[new_segment].goto(new_x, new_y)
    segments[0].forward(20)
screen.exitonclick()