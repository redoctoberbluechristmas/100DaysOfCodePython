
import another_module
from turtle import Turtle, Screen

print(another_module.another_variable)

# Instantiate an object of the Turtle class, imported from the turtle module, in an object named timmy.
timmy = Turtle()
john = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("aquamarine4")

john.shape("turtle")
john.color("red")


def timmy_star():
    for i in range(0, 101):
        timmy.forward(100)
        timmy.left(25)
        timmy.back(100)


def john_star():
    for i in range(0, 101):
        john.back(100)
        john.right(25)
        john.forward(100)


timmy_star() and john_star()

my_screen = Screen()

my_screen.exitonclick()
