"""Hirst Painting Project"""

import colorgram
import turtle, random
from turtle import Turtle, Screen

turtle.colormode(255)

def get_valid_colors(image, amount_colors):
    colors = colorgram.extract(image, amount_colors)
    color_list = []
    for color in colors:
        if color.rgb[0] < 250 and color.rgb[1] < 250 and color.rgb[2] < 250:
            color_list.append(color.rgb)
    return color_list

def doing_points(rows, columns, gap, size, obj_turtle, image, amount_colors):
    colors = get_valid_colors(image, amount_colors)
    for row in range(rows):
        last_position = obj_turtle.pos()
        for column in range(columns):
            obj_turtle.penup()
            obj_turtle.forward(gap)
            obj_turtle.dot(size, colors[random.randint(0, len(colors) - 1)])
        obj_turtle.penup()
        obj_turtle.setposition(last_position)
        obj_turtle.left(90)
        obj_turtle.forward(gap)
        obj_turtle.right(90)

def set_initial_position(obj_turtle, x, y):
    obj_turtle.speed("fastest")
    obj_turtle.penup()
    obj_turtle.setposition(x, y)

reptile_pet = Turtle()
set_initial_position(reptile_pet, -150, 0)
doing_points(10, 10, 20, 10, reptile_pet, "./hirst_painting.jpeg", 20)

screen = Screen()
screen.exitonclick()
