from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):   #<-- Whenever you intialize a new object from class, init gets called and does everything.
        # Methods can be invoked at init, but they don't have to be.
        super().__init__()    #<--- Calling the super class, Turtle.
        self.shape("circle")   #<--- This is a method inherited from Turtle.
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) #<--- halving the default length of the shapesize
        # (20 x 20 pixels) from Turtle class
        self.color("blue")
        self.speed("fastest")
        self.go_random_location()

    def go_random_location(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
