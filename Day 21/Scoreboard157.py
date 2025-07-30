"""Scoreboard class"""
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 14, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.current_score = 0
        self.refresh()
    def set_score(self, point):
        self.current_score += point
    def get_score(self):
        return self.current_score
    def refresh(self):
        self.clear()
        self.write(arg=f"Score: {self.get_score()}", move=False, align=ALIGNMENT, font=FONT)
    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"Game Over", move=False, align=ALIGNMENT, font=FONT)
