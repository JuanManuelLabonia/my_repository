from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20,"")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.write_score()
    
    def write_score(self):
        self.goto(-10, 270)
        self.write(f"Score: {self.score}", align= ALIGNMENT, font= FONT)    
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER.", align= ALIGNMENT, font= FONT)
    
    def refresh(self):
        self.score += 1
        self.clear()
        self.write_score()
