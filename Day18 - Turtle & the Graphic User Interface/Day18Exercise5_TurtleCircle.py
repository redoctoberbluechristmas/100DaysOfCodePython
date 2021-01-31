import turtle as t
import random

t.colormode(255)

tim = t.Turtle()
tim.shape("turtle")

shape = ["turtle", "arrow", "circle", "square", "triangle", "classic"]
speed = ["slowest", "slow", "normal", "fast", "fastest"]
#colors = ["blue", "maroon", "dark goldenrod", "teal", "black", "yellow", "deep pink", "indigo"]
headings = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size):
    return 360 / size

# TODO Draw a circle, determine how large it will be; each circle will be random in color.
tim.speed("fastest")


size = 360
for i in range(size):
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(tim.heading() + draw_spirograph(size))

screen = t.Screen()
screen.exitonclick()
