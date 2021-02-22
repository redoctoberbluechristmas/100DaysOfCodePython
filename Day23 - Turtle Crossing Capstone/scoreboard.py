from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-200, 250)
        self.write(f"Level = {self.level}", align="center", font=FONT)

    def score_point(self):
        self.clear()
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER!", align="center", font=FONT)
