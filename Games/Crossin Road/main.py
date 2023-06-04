import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkeypress(fun = player.move_up, key = "Up")
screen.onkeypress(fun = player.move_up, key = "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.generate_a_car()
    car_manager.move_car()
    
    if player.ycor() > 270:
        time.sleep(0.3)
        player.go_home()
        car_manager.speed_up()
        scoreboard.level_up()
    
    for car in car_manager.car_list:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
    
    
