from turtle import Turtle

FONT = ("Courier", 14, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-285, 270)
        self.show_score()

    def level_up(self):
        self.level += 1
        self.show_score()
    
    def show_score(self):
        self.clear()
        self.write(f"Level: {self.level}", font = FONT)
    
    def game_over(self):
        self.goto(-50,0)
        self.write("GAME OVER.", font = FONT)     
