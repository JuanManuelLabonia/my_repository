from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
CAR_RAIL = [-260, -240, -220, -200, -180, -160, -140, -120, -100, -80, -60, -40, 
            -20, 0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    
    def __init__(self):
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate_a_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle("square")
            car.penup()
            car.shapesize(stretch_len= 2, stretch_wid= 1)
            car.color(random.choice(COLORS))
            car.goto(300, y = random.choice(CAR_RAIL))
            self.car_list.append(car)
        
    def move_car(self):
        for car in self.car_list:
            car.backward(self.car_speed)
    
    def speed_up(self):
        self.car_speed += MOVE_INCREMENT
    




    
    
