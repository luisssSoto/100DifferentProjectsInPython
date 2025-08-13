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
        with open("highscore.txt", "r") as high_score_file:
            self.high_score = high_score_file.read()
        self.refresh()
    def set_score(self, point):
        self.current_score += point
    def get_score(self):
        return self.current_score
    def refresh(self):
        self.clear()
        self.write(arg=f"Score: {self.get_score()} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)
    def reset(self):
        if self.current_score > int(self.high_score):
            self.high_score = self.current_score
            with open("highscore.txt", "w") as high_score_file:
                high_score_file.write(str(self.high_score))
        self.current_score = 0
        self.refresh()
