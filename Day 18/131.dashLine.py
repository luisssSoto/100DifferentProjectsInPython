"""Dash line with turtle module"""
from turtle import Turtle, Screen

turtle = Turtle()
turtle.color("orange")
turtle.shape("turtle")
turtle.pensize(3)

def dash_line(obj_turtle):
    for _ in range(20):
        obj_turtle.forward(5)
        obj_turtle.penup()
        obj_turtle.forward(5)
        obj_turtle.pendown()

def dashed_square(obj_turtle):
    for _ in range(4):
        dash_line(obj_turtle)
        obj_turtle.right(90)

dashed_square(turtle)

screen = Screen()
screen.exitonclick()