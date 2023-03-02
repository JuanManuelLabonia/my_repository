from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_R = 0
        self.score_L = 0
        self.reload()
    
    def reload(self):
        self.clear()
        self.goto(0, 255)
        self.write(f"{self.score_L}\t{self.score_R}", align = "center", font = ("Courier", 30, "bold"))
        
    def left_scored(self):
        self.score_L += 1
        self.reload()
    
    def right_scored(self):
        self.score_R += 1
        self.reload()