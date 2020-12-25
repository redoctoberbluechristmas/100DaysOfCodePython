print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#This will convert input to lower, and look for anything like "left"
left_or_right = ((input('You\'re at a crossroads. Would you like to go "left" or "right"?\n')).lower()).find("left")

# If left_or_right does not NOT (!= -1) contain "left", you turn left. If it comes back 0, you turn not left (or right)
if(left_or_right != -1):
  print("You turn left. You're at a beach. There's an island in the distance, but it's pretty far and the water looks rough.")
  swim_or_wait = ((input("Would you like to swim across or wait?\n")).lower()).find("wait")
  if(swim_or_wait != -1):
    print("You decide to wait. Eventually, a boat appears and takes you to the island. On the island, you find a wall with three doors. One is red, one is yellow, and one is blue.")
    which_door = ((input("Which door do you choose? Red, Yellow, or Blue?\n")).lower()).find("yellow")
    if(which_door != -1):
      print("There is a treasure behind the yellow door. You win!")
    else:
      print("Sorry, you triggered a trap. Game Over!")
  else:
    print("You tried to swim, but ran out of energy and died. Game over.")
else:
  print("Some lion ate you, game over.")