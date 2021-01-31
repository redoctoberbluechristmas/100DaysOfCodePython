from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")

colors = ["blue", "maroon", "dark goldenrod", "teal", "black", "yellow", "deep pink", "indigo"]

# def random_color():
#     r = random.randint(0, 256)
#     g = random.randint(0, 256)
#     b = random.randint(0, 256)
#     return tim.pencolor(r, g, b)


def draw_sides(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        tim.forward(100)
        tim.left(angle)


sides = [3, 4, 5, 6, 8, 9, 10]

for i in sides:
    tim.color(random.choice(colors))
    draw_sides(i)