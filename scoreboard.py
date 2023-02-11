from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def score_update(self):
        self.score += 1

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.write_score()
