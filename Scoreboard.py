from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):

        super().__init__()
        self.score = 0
        self.highScore = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.updateScore()

    def updateScore(self):

        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highScore}", align="center", font=("Arial", 24, "normal"))

    def reset(self):
        
        if self.score > self.highScore:
            self.highScore = self.score
        
        self.score = 0
        self.updateScore()

    def addPoint(self):

        self.score += 1
        self.clear()
        self.updateScore()