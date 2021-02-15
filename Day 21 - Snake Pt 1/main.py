from turtle import Turtle, Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)

screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


# Initializing Object Block
snake = Snake()
food = Food()
scoreboard = Scoreboard()
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
        scoreboard.add_score()
        snake.extend()
        food.go_random_location()

    # Detect collision with wall.
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        scoreboard.game_over()
        game_on = False


    # Detect collision with tail.    INTRODUCE SLICING.
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_on = False


screen.exitonclick()

