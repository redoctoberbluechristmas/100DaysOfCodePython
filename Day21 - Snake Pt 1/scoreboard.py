from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 16, "normal")
GAMEOVER_FONT = ("Courier", 42, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setpos(x=0, y=260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score = {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER!", align=ALIGN, font=GAMEOVER_FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
