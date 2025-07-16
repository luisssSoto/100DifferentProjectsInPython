"""Drawing Different Shapes"""
import turtle
from turtle import Turtle, Screen
import random

t = Turtle()
t.shape("turtle")

def set_degrees(sizes):
    return 360 / sizes

def choose_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb_colors = (r, g, b)
    return rgb_colors

def draw_shapes(sizes, obj_turtle):
    turtle.colormode(255)
    obj_turtle.pencolor(choose_color())
    for times in range(sizes):
        obj_turtle.forward(100)
        obj_turtle.right(set_degrees(sizes))

for size in range(3, 11):
    draw_shapes(size, t)

s = Screen()
s.exitonclick()