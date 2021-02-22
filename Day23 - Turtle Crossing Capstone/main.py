import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")


game_is_on = True
while game_is_on:    #<-- everything in the while loop will run every 0.1 seconds.
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()




    # Detect collision with car. "car_manager" is the object - the individual cars are not objects. They belong to the
    # car_manger's all_cars list.
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect turtle makes it to top.
    if player.is_at_finish_line():
        scoreboard.score_point()
        player.return_to_start()
        car_manager.speed_cars()


screen.exitonclick()