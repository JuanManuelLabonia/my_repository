from turtle import Turtle

lines = "|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n"

class Line(Turtle):
    def __init__(self, x_axis, y_axis, width):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x_axis, y_axis)
        self.write(f"{lines}", align = "center", font = ("Courier", width, "bold"))