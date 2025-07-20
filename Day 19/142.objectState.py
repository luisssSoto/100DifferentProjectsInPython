"""Object State"""

from turtle import Turtle, Screen

"""Different states (attributes and methods) has each instance"""
my_screen = Screen()
my_screen.setup(800, 600)

leo = Turtle()
leo.shape("turtle")
leo.color("blue")

raphael = Turtle()
raphael.shape("turtle")
raphael.color("red")
raphael.penup()
raphael.setposition((0, -50))

my_screen.exitonclick()