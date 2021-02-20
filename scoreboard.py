from turtle import Turtle

FONT = ("Arial", 15, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.score = -1
        self.penup()
        self.goto(0, 278)
        self.refresh()

    def refresh(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", move=False, align=ALIGNMENT, font=FONT)
