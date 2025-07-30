"""Move a snake with arrow keys"""
from turtle import Screen
from Snake155 import Snake
from Food155 import Food
from Scoreboard155 import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


my_snake = Snake()
my_food = Food()
my_scoreboard = Scoreboard()

screen.listen()
screen.onkey(my_snake.up, "Up")
screen.onkey(my_snake.down, "Down")
screen.onkey(my_snake.left, "Left")
screen.onkey(my_snake.right, "Right")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    my_snake.move()
    if my_snake.head.distance(my_food) < 15:
        my_food.refresh()
        my_scoreboard.set_score(1)
        my_scoreboard.refresh()

screen.exitonclick()
