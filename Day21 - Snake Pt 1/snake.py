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
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.snake_body.append(new_segment)

    def extend(self):
        self.add_segment(self.snake_body[-1].position()) # position() method comes from turtle class.

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
