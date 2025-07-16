"""Draw a Square Challenge"""

from turtle import Turtle, Screen

tiny_turtle = Turtle()
tiny_turtle.shape("turtle")
tiny_turtle.color("coral")

def draw_a_square(obj_turtle):
    for _ in range(4):
        obj_turtle.forward(100)
        obj_turtle.right(90)

draw_a_square(tiny_turtle)



screen = Screen()
screen.exitonclick()