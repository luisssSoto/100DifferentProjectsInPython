"""Main"""
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from time import sleep

screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.tracer(0)


right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
sc = Scoreboard()

screen.listen()

screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

is_game_over = False
while not is_game_over:
    sleep(ball.increase_speed)
    screen.update()
    ball.move()

    # Detect collision with the walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with the paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if the ball goes beyond the right paddle
    if ball.xcor() > 380:
        ball.restart()
        sc.left_score_increased()

    # Detect if the ball goes beyond the left paddle
    if ball.xcor() < -380:
        ball.restart()
        sc.right_score_increased()








screen.exitonclick()