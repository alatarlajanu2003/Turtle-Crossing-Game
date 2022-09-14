from turtle import Turtle

FONT = ("Courier", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-280, 250)
        self.update()

    def update(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", align="left", font=FONT)
        self.level += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER!", align="center", font=FONT)