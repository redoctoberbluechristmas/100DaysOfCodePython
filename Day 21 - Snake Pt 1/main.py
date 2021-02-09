from turtle import Turtle, Screen
from time import sleep
from snake import Snake


screen = Screen()
screen.setup(width=600, height=600)

screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

screen.update()

game_on = True

while game_on:
    screen.update()
    sleep(0.1)

    snake.move()

screen.exitonclick()

