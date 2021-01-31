import colorgram
import turtle as t
import random

t.colormode(255)

tim = t.Turtle()
tim.shape("turtle")
tim.speed("fastest")

headings = [0, 90, 180, 270]


Extracting colors from Hirst
colors = colorgram.extract('hirst.jpg', 25)
rgb = []

for i in colors:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    if r and g and b < 240:
        new_color = (r, g, b)
        rgb.append(new_color)

print(rgb)

rgb_cleaned = [(201, 164, 112), (239, 246, 241), (152, 75, 50), (221, 201, 138), (57, 95, 126), (170, 152, 44), (138, 31, 20), (135, 163, 183), (196, 94, 75), (49, 121, 88), (143, 177, 149), (95, 75, 77), (76, 39, 32), (164, 146, 157), (16, 98, 71), (232, 176, 165), (54, 46, 48), (32, 61, 76), (22, 83, 89), (182, 204, 176), (141, 22, 25), (86, 147, 127)]


# def draw_spirograph(size):
#     return 360 / size


# size = 20
# for i in range(size):
#     tim.color(random.choice(rgb_cleaned))
#     tim.circle(100)
#     tim.setheading(tim.heading() + draw_spirograph(size))
#
# screen = t.Screen()
# screen.exitonclick()
