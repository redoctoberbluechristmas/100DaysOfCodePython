from turtle import Turtle, Screen
from time import sleep
from snake import Snake
from food import Food


screen = Screen()
screen.setup(width=600, height=600)

screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


# Initializing Object Block
snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



screen.update()

game_on = True

while game_on:
    screen.update()
    sleep(0.1)

    snake.move()

    # Detect collision with food using turtle.distance() method.
    if snake.head.distance(food) < 15:
        print("nom nom nom")
        food.go_random_location()

screen.exitonclick()

