from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

predicted_winner = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?")


turtle_names = ["tim", "tom", "terry", "ted", "tank", "toodles"]
colors = ["red", "orange", "yellow", "green", "blue", "indigo"]
all_turtles = []

y_pos = [-70, -40, -10, 20, 50, 80]

for i in range(len(turtle_names)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[i])
    all_turtles.append(new_turtle)

if predicted_winner:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == predicted_winner:
                print(f"The {winning_color} turtle won! Congratulations.")
            else:
                print(f"The {predicted_winner} turtle did not win. The {winning_color} turtle won.")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)




screen.exitonclick()
