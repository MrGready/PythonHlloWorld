from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.pu()
        self.hideturtle()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def level_up(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.clear()
        self.goto(0, 100)
        self.write("GAME OVER", align="center", font=FONT)