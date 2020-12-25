rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# Store a list of variables
game_images = [rock, paper, scissors]
import random

player_choice = input("What do you choose? Rock, paper, or scissors?  ").lower()

print(player_choice)

if player_choice.startswith("r"):
  player_choice = 0
  print("You chose rock.")
elif player_choice.startswith("p"):
  player_choice = 1
  print("You chose paper.")
elif player_choice.startswith("s"):
  player_choice = 2
  print("You chose scissors.")
else:
  print("Please make a valid choice.")
  exit()

#Print picture based on player choice.
print(game_images[player_choice])

computer_choice = random.randint(0, 2)

if(computer_choice == 0):
  print("The computer chose rock.")
elif(computer_choice == 1):
  print("The computer chose paper.")
else:
  print("The computer chose scissors.")

#Print picture for computer choice.
print(game_images[computer_choice])

if player_choice == 0 and computer_choice == 2:
  print("You win!")
elif player_choice > computer_choice:
  print("You win!")
elif player_choice == computer_choice:
  print("You tie.")
else:
  print("Computer wins.")