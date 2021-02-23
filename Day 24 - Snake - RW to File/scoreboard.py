from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 16, "normal")
GAMEOVER_FONT = ("Courier", 42, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(self.read_high_score())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setpos(x=0, y=260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} High Score = {self.high_score}", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_new_high_score(self.high_score)
        self.score = 0
        self.update_scoreboard()

    def add_score(self):
        self.score += 1
        self.update_scoreboard()

    def write_new_high_score(self, high_score):
        with open("high_score.txt", mode="w") as file:
            file.write(str(high_score))

    def read_high_score(self):
        with open("high_score.txt", mode="r") as file:
            return file.read()

