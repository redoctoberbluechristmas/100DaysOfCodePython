from turtle import Turtle

# In Python, constants are spelt with all caps, snake case.
# Reason to have constants is so that you don't have to dig through code to make minor changes.
# These are things which will remain the same NO MATTER HOW MANY OBJECTS you produce.

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_body = []

        # Can call methods when you initialize object of class.
        self.create_snake()

        # Replacing self.snake_body[0] in code so I don't have to write it out every time.
        # Make sure to put self.head below self.snake_body and self.create_snake(), because this attribute references
        # snake_body, and won't exist prior to those two.

        self.head = self.snake_body[0]

    def create_snake(self):

        for i in STARTING_POSITIONS:
            snake_body_segments = Turtle(shape="square")
            snake_body_segments.color("white")
            snake_body_segments.penup()
            snake_body_segments.goto(i)
            self.snake_body.append(snake_body_segments)

    def move(self):

        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg_num - 1].xcor()
            new_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)
        # Need to continue to propel the first segment, outside of the for loop, for the snake to move forward.
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
