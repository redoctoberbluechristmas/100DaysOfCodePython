# Script to get robot to jump hurdles, here: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
# Listen intended to teach functions.

def turn_right():
    for i in range(0, 3):
        turn_left()

# This isn't necessary to meet the challenge, especially given the challenge's short length, it just bothered me when I
# saw repeatable steps that weren't reduced to a function.
def move_left():
    move()
    turn_left()
    
def move_right():
    move()
    turn_right()

def jump():
    move_left()
    move_right()
    move_right()
    move_left()

for i in range(0, 6):
    jump()
    print(i)
