import time
from turtle import Screen
from player import Player, FINISH_LINE_Y, STARTING_POSITION
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

my_turtle = Player()

screen.listen()
screen.onkey(my_turtle.move_forward, "Up")

my_car_manager = CarManager()
my_scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # moving cars process
    for i in range(len(my_car_manager.cars)):
        my_car_manager.cars[i].move_forward()

        # scenario when a car crash against the player
        if my_turtle.distance(my_car_manager.cars[i]) < 20:
            game_is_on = False
            my_scoreboard.game_over()

        if my_car_manager.cars[i].xcor() < -320:
            my_car_manager.recycle_cars(i)

    # scenario after each next level
    if my_turtle.distance(0, FINISH_LINE_Y) <= 10:
        my_scoreboard.next_level()
        my_turtle.goto(STARTING_POSITION)
        my_car_manager.move_next_level()

screen.exitonclick()





