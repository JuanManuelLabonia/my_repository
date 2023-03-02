from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed_amount = 0.036
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    def bounce(self, x_dir, y_dir):
        """Requieres x_dir and y_dir that need to be 1 or -1 to change the bouncing direction"""
        self.x_move *= x_dir
        self.y_move *= y_dir
        self.speed_amount *= 0.95
    
    def reset(self):
        self.goto(0,0)
        self.bounce(-1, 1)
        self.speed_amount = 0.036






