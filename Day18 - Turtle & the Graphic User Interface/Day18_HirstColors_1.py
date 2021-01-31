import colorgram
import turtle as t
import random

t.colormode(255)

tim = t.Turtle()
tim.shape("turtle")
tim.speed("fastest")

headings = [0, 90, 180, 270]


colors = colorgram.extract('hirst.jpg', 3)

def hirst_color():
    return(colors[random.randint(0, len(colors) - 1)].rgb)


def draw_spirograph(size):
    return 360 / size


size = 20
for i in range(size):
    tim.color(hirst_color())
    tim.circle(100)
    tim.setheading(tim.heading() + draw_spirograph(size))

screen = t.Screen()
screen.exitonclick()
