"""Random Walk"""
'''Set up turtle module to accept 0-255 r, g, b colors'''
import turtle
turtle.colormode(255)

from turtle import Turtle, Screen
import random
gary = Turtle()
gary.shape("square")
gary.color("green")

def walking_randomly(obj_turtle):
    obj_turtle.pensize(15)
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    obj_turtle.color(red, green, blue)
    obj_turtle.speed(0)
    steps = random.randint(1, 100)
    direction = random.choice([0, 90, 180, 270])
    obj_turtle.forward(steps)
    obj_turtle.right(direction)

def num_times(obj_turtle):
    for _ in range(random.randint(40, 60)):
        walking_randomly(obj_turtle)

num_times(gary)





screen = Screen()
screen.exitonclick()