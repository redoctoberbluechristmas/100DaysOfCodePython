# Used in exercise here: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    
    turn_left()
    while wall_on_right():
        if front_is_clear():
            move()
        else:
            turn_left()
    turn_right()
    move()
    turn_right()
    
while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()