"""Create a screen and a body head"""
from turtle import Screen
from Snake149 import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

my_snake = Snake()

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    my_snake.move()
screen.exitonclick()