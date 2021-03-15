import pandas
import turtle

screen = turtle.Screen()
screen.title("US Map Game")

# Load image as a new shape for Turtle to work with.
image = "blank_states_img.gif"
screen.addshape(image)

# Pulls-up image of US map when run
turtle.shape(image)

# Import data from CSV; convert to DataFrame
data = pandas.read_csv("50_states.csv")

all_states = data.state.to_list()



#######################################################################################
# How to harvest click coords
#######################################################################################

# Find coordinates of each state (get mouse click coordinates on each state)
# X and Y values are already in CSV, but this is how you do it.
# def get_mouse_click_coord(x,y):
# #     print (x,y)
# #
# # turtle.onscreenclick(get_mouse_click_coord)  # onscreenclick is an event listener.
# # turtle.mainloop() # alternative way to keep screen open despite exit on click.

#######################################################################################
# End section on harvesting click coordinates
#######################################################################################

guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Guess another state").title() # Creates pop-up box asking for input
    #answer_state = answer_state.lower()
    #print(answer_state)

    # Try saving each state as an "object" in a class called state, inheriting from Turtle. Pass X, Y coords.

    if answer_state == "Exit":
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        # missing states = [new_item for item in all_states if test]
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")


        missing states = [     state in all_states if state not in guessed_states]

        break

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

        # To get raw value from dataframe:
        #  state_data.state.item()  < --- use item() method
        # Write data['state'] to data['x', 'y']


# states_to_learn.csv


