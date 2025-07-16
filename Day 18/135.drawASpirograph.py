"""Draw a Spirograph"""
import turtle
import random
from turtle import Turtle, Screen

torti = Turtle()
torti.shape("turtle")
torti.color("green")
torti.speed(0)

def choosing_random_color():
    turtle.colormode(255)
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return red, green, blue

def drawing_circle(obj_turtle, radius, gap):
    for i in range(int(360 / gap)):
        obj_turtle.color(choosing_random_color())
        obj_turtle.circle(radius)
        obj_turtle.setheading(obj_turtle.heading() + gap)

drawing_circle(torti, 150, 5)

screen = Screen()
screen.exitonclick()