
# From Day 16 onwards, you will be creating your own PyCharm projects from scratch.
# Instead of using templates that I have created for you.
# It will be another step in your journey as a developer!
# But don't worry, I will explain how to do everything in the video tutorials on Udemy.
# 1. part
from turtle import Turtle
tiny_turtle = Turtle()
print(tiny_turtle)

# 2. part Attributes
from turtle import Screen
my_screen = Screen()
print(my_screen)
# Attributes
print(my_screen.canvheight)

# 3. part Methods
tiny_turtle.shape("turtle")
tiny_turtle.color("DarkGreen")
tiny_turtle.forward(100)
my_screen.exitonclick()
