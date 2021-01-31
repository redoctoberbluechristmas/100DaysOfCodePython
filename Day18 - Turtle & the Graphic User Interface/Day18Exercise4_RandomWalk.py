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
    random_color = (r, g, b)
    return random_color


for i in range(1000):
    tim.color(random_color())
    tim.shape(random.choice(shape))
    tim.speed(random.choice(speed))
    tim.pensize(random.randint(0, 20))
    tim.forward(20)
    tim.setheading(random.choice(headings))

screen = t.Screen()
screen.exitonclick()
