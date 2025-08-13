"""Final Version"""
from turtle import Screen
from Snake158 import Snake
from Food158 import Food
from Scoreboard158 import Scoreboard
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
    # Detect collision with food
    if my_snake.head.distance(my_food) < 15:
        my_food.refresh()
        my_snake.extend()
        my_scoreboard.set_score(1)
        my_scoreboard.refresh()
    # Detect collision with wall
    if my_snake.head.xcor() > 280 or my_snake.head.xcor() < -280 or my_snake.head.ycor() > 280 or my_snake.head.ycor() < -280:
        my_scoreboard.reset()
        my_snake.reset()
    # Detect collision with snake's body
    for segment in my_snake.segments[1 : ]:
        if my_snake.head.distance(segment) < 10:
            my_scoreboard.reset()
            my_snake.reset()

screen.exitonclick()
