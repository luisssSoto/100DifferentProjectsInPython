"""Etch Sketch App"""

from turtle import Turtle, Screen

my_turtle = Turtle()
start_position = my_turtle.heading()
def go_straight():
    my_turtle.forward(10)
def go_backward():
    my_turtle.backward(10)
def go_left():
    my_turtle.left(10)
def go_right():
    my_turtle.right(10)
def return_home():
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()
    my_turtle.clear()

my_screen = Screen()
my_screen.listen()
my_screen.onkey(go_straight, "w")
my_screen.onkey(go_backward, "s")
my_screen.onkey(go_left, "a")
my_screen.onkey(go_right, "d")
my_screen.onkey(return_home, "c")
my_screen.exitonclick()