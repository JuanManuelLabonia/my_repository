from Hirst_painting import rgb
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.hideturtle()
screen = Screen()
screen.colormode(255)
tim.pencolor(255, 255, 255)
tim.speed("fastest")

while True:
    tim.setx(-228)
    tim.sety(-228)
    for i in range(10):
        for i in range(10):
            tim.dot(20, random.choice(rgb))
            tim.penup()
            tim.forward(50)
            tim.pendown()
        if tim.heading() == 0:
            tim.setheading(90)
            tim.penup()
            tim.forward(50)
            tim.setheading(180)
            tim.forward(50)
        else:
            tim.setheading(90)
            tim.penup()
            tim.forward(50)
            tim.setheading(360)
            tim.forward(50)
    tim.clear()

    
    



