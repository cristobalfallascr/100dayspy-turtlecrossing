from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "black", "blue", "purple"]
STARTING_MOVE_DISTANCE = 80
MOVE_INCREMENT = 10




class CarManager ():
    def __init__(self):

        self.cars = []





    def create_car(self,  random_x, random_y):
        new_car = Turtle(shape="square")
        new_car.color(COLORS[random.randint(0,5)])
        new_car.shapesize(stretch_len=2, stretch_wid=1,)
        new_car.penup()
        new_car.setheading(180)
        new_car.goto(random_x, random_y)
        self.cars.append(new_car)


    def generate_cars(self):

                random_y = random.randrange(-240, 260, 22)
                random_x = random.randrange(290, 390, 22)
                self.create_car(random_x, random_y)



    def move_cars(self):
        for car in self.cars:
            print(car)
            car.forward(STARTING_MOVE_DISTANCE)
