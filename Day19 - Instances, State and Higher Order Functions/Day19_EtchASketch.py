from turtle import Turtle, Screen


tim = Turtle()
tim.shape("turtle")
tim.color("red")

screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

# When using a function as a parameter in another function, don't put the () after it.

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=left)
screen.onkey(key="d", fun=right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()