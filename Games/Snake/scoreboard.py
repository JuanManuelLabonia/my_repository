from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20,"")
with open(r"C:\Users\JML\Desktop\Python\Python Course\Prácticas y proyectos\Week 4\Day 24\score.txt") as file:
    HIGH_SCORE = int(file.read())

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = HIGH_SCORE
        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}\tHigh Score: {self.high_score}", align= ALIGNMENT, font= FONT)

    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        with open(r"C:\Users\JML\Desktop\Python\Python Course\Prácticas y proyectos\Week 4\Day 24\score.txt", mode = "w") as file:
            file.write(f"{self.high_score}")
        self.update_scoreboard()
    
    def refresh(self):
        self.score += 1
        self.update_scoreboard()
