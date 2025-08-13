"""Snake class"""
from turtle import Turtle

COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVES = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for x in COORDINATES:
            self.add_segment(x)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for new_segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[new_segment - 1].xcor()
            new_y = self.segments[new_segment - 1].ycor()
            self.segments[new_segment].goto(new_x, new_y)
        self.segments[0].forward(MOVES)

    def reset(self):
        for segment in self.segments:
            segment.goto((1000, 1000))
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

