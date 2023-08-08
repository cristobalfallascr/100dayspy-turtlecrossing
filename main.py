import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
new_player = Player()
game_cars = CarManager()



screen.listen()
screen.onkey(new_player.cross, "Up")
loop = 0
game_is_on = True
while game_is_on:
    screen.update()
    if loop % 6 == 0:
        game_cars.generate_cars()
        game_cars.move_cars()
    time.sleep(0.1)
    loop += 1





screen.exitonclick()