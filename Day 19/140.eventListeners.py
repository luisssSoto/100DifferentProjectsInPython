"""Event Listeners and Higher Order Functions"""

from turtle import Turtle, Screen

my_turtle = Turtle()

def move_forward():
    my_turtle.forward(10)

my_screen = Screen()
my_screen.listen()
my_screen.onkey(move_forward, "space")
my_screen.exitonclick()