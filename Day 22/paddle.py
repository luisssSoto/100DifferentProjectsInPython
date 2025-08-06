"""Paddle Class"""

from turtle import Turtle

STEPS = 20

class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)
        self.speed("fastest")
        self.penup()
        self.goto(coordinates)
    def up(self):
        self.goto((self.xcor(), self.ycor() + 20))
    def down(self):
        self.backward(STEPS)

