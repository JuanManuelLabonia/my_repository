from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width = 500, height = 400)
is_race_on = False
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [125, 75, 25, -25, -75, -125]
list_of_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x = -230, y = y_positions[turtle_index])
    list_of_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in list_of_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if user_bet == winning_color:
                print(f"You've won! The {winning_color} turtle won the race!")
            else:
                print(f"You've lost. The {winning_color} turtle won the race!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()