"""Snake class"""
from turtle import Turtle

COORDINATES = [x for x in range(0, -41, -20)]
MOVES = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for x in COORDINATES:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(x, 0)
            self.segments.append(new_segment)

    def move(self):
        for new_segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[new_segment - 1].xcor()
            new_y = self.segments[new_segment - 1].ycor()
            self.segments[new_segment].goto(new_x, new_y)
        self.segments[0].forward(MOVES)
