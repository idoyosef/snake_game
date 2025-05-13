from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.goto(0, 270)
        self.score = 0
        self.high_score = 0
        file = open("data.txt", 'r')
        saved_score = file.read()
        if int(saved_score) > self.high_score:
            self.high_score = int(saved_score)
        self.pencolor("white")
        self.speed("fastest")
        self.print_score()

    def print_score(self):
        self.write(f"Score : {self.score}, High Score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER.", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score = self.score+1

        if self.score > self.high_score:
            self.high_score = self.score
            file = open("data.txt", 'w')
            file.write(str(self.score))
        self.print_score()