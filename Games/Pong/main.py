from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
from line import Line
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)
screen.listen()

paddle_L = Paddle(-350, 0)
paddle_R = Paddle(350, 0)
ball = Ball()
scoreboard = Scoreboard()
middle_line = Line(x_axis = 0, y_axis = -340, width = 30)
left_line = Line(x_axis = -348, y_axis = -340, width = 10)
right_line = Line(x_axis = 352, y_axis = -340, width = 10)


screen.onkeypress(paddle_L.down, key="s")
screen.onkeypress(paddle_L.up, key="w")      
screen.onkeypress(paddle_R.down, key="Down")
screen.onkeypress(paddle_R.up, key="Up")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.speed_amount)
    ball.move()
    
    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        time.sleep(0.02)
        ball.bounce(1, -1)
    #Detect collision with right paddle
    elif (ball.distance(paddle_R) < 65 and ball.xcor() > 330 and ball.xcor() < 350) or (ball.distance(paddle_L) < 65 and ball.xcor() < -330 and ball.xcor() > -350):
        ball.bounce(-1, 1)
        time.sleep(ball.speed_amount)

    #Restart game
    elif ball.xcor() > 385:
        ball.reset()
        scoreboard.left_scored()
        time.sleep(ball.speed_amount)
        
    elif ball.xcor() < -385:
        ball.reset()
        scoreboard.right_scored()
        time.sleep(ball.speed_amount)


        




screen.exitonclick()
