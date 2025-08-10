from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(choice(COLORS))
        self.penup()
        self.setheading(180)
        self.speed = STARTING_MOVE_DISTANCE
        self.goto(randint(-200, 800), randint(-240, 250))

    def move_forward(self):
        self.forward(self.speed)

    def reset_position(self):
        self.goto(randint(300, 800), randint(-240, 250))

class CarManager:
    def __init__(self):
        self.cars = []
        for _ in range(30):
            self.cars.append(Car())

    def recycle_cars(self, index):
        self.cars[index].color(choice(COLORS))
        self.cars[index].reset_position()

    def move_next_level(self):
        for car in self.cars:
            car.goto(randint(-200, 800), randint(-240, 250))
            car.speed += MOVE_INCREMENT






