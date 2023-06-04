from turtle import Turtle, Screen

screen = Screen()

class Paddle(Turtle):
    def __init__(self, position_x, position_y):
        super().__init__(shape = "square")
        self.position_x = position_x
        self.position_y = position_y
        self.penup()
        self.color("white")
        self.goto(self.position_x, self.position_y)
        self.shapesize(stretch_wid=5, stretch_len=1)
    
    def up(self):
        if self.ycor() < 242:
            self.position_y += 20
            self.goto(self.position_x, self.position_y)
    
    def down(self):
        if self.ycor() > -238:
            self.position_y -= 20
            self.goto(self.position_x, self.position_y)

