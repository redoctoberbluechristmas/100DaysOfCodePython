# Used with problem here: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

## This new while loop added to break out of getting stuck

while front_is_clear():
    move()
turn_left()

# This is my original solution.
while not at_goal():
    if wall_on_right() and front_is_clear():
        move()
    elif right_is_clear():
        turn_right()
        move()
    elif wall_on_right() and wall_in_front():
        turn_left()


# This is a cleaner solution, but I like mine.

# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left