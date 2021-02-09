
from turtle import Turtle


class Snake:
    def __init__(self):
        snake_body = []

    starting_positions = [(0, 0), (-20, 0), (-40, 0)]
    snake_body = []

    for i in starting_positions:
        snake_body_segments = Turtle(shape="square")
        snake_body_segments.color("white")
        snake_body_segments.penup()
        snake_body_segments.goto(i)
        snake_body.append(snake_body_segments)

    def move(self):

        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg_num - 1].xcor()
            new_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)
        # Need to continue to propel the first segment, outside of the loop, for the snake to move forward.
        self.snake_body[0].forward(20)
